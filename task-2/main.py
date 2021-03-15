from bs4 import BeautifulSoup
import unittest


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
        soup = BeautifulSoup(f, 'lxml')
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


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
