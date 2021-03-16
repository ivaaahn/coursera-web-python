from bs4 import BeautifulSoup as bs
import unittest
import re
import os


def get_max_seq(body):
    max_count = 0
    curr = body.find('a')

    while curr and "bodyContent" in [p.get('id') for p in curr.parents]:
        curr_count = 1

        next = curr.find_next_sibling()
        while next and next.name == 'a':
            curr_count += 1
            curr = next
            next = curr.find_next_sibling()
        else:
            max_count = max(curr_count, max_count)
            curr = curr.find_next('a')

    return max_count


def calc_lists(body):
    return sum(1 for l in body.find_all(['ul', 'ol'])
               if 'ul' not in [p.name for p in l.parents] and
               'ol' not in [p.name for p in l.parents])


def parse(path_to_file: str) -> list:
    with open(path_to_file, 'r', encoding='utf-8') as f:
        soup = bs(f, 'lxml')
        body = soup.find('div', id='bodyContent')

        imgs = list(body.find_all('img'))
        img_widths = [int(img.get('width'))
                      for img in imgs if img.get('width') is not None]
        ans_imgs = sum(1 for width in img_widths if width >= 200)

        hdrs = body.find_all(['h'+str(i) for i in range(1, 7)])
        ans_headers = sum(1 for hdr in hdrs if hdr.text[0] in 'ETC')

        ans_linkslen = get_max_seq(body)
        ans_lists = calc_lists(body)

    return [ans_imgs, ans_headers, ans_linkslen, ans_lists]


def get_all_links(path, page):
    with open(path + page, 'r', encoding='utf-8') as f:
        soup = bs(f, 'lxml')
        body = soup.find('div', id='bodyContent')

        hrefs = [a.get('href') for a in body.find_all('a')]
        pattern = r"/wiki/(?!Category:).+"
        wikis = os.listdir(path)

    l = list(set([h for h in hrefs if h and re.match(
        pattern, h) and h.lstrip('/wiki/') in wikis]))

    return [h.lstrip('/wiki/') for h in l]


def backtrace(parent, start, end):
    path = [end]

    while path[-1] != start:
        path.append(parent[path[-1]])

    path.reverse()

    return path


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    adj = {f'{start_page}': get_all_links(path, start_page)}
    lvl = {f'{start_page}': 0}

    parent = {}
    start = start_page
    queue = [start]

    while queue:
        v_curr = queue.pop(0)

        if v_curr == end_page:
            return backtrace(parent, start_page, end_page)

        if not adj.get(v_curr):
            adj[v_curr] = get_all_links(path, v_curr)

        for w in adj.get(v_curr):
            if lvl.get(w) is None:
                parent[w] = v_curr
                queue.append(w)
                lvl[w] = lvl[v_curr] + 1


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    pages = build_bridge(path, start_page, end_page)

    statistic = dict()

    for page in pages:
        statistic[page] = parse(path + page)

    return statistic


# ans = get_statistics('wiki/', 'Stone_Age', 'Python_(programming_language)')


# for key, value in ans.items():
#     print(f"{key}: {value}")
