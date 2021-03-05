from requests import get
import requests as req
from operator import itemgetter

from .settings import API_VERSION, ACCESS_TOKEN


CURR_YEAR = 2021


def get_id(username: str) -> str:
    url_req = 'https://api.vk.com/method/users.get'
    params = {'user_ids': username,
              'access_token': ACCESS_TOKEN, 'v': API_VERSION}
    response = get(url_req, params=params)

    if response.ok:
        return response.json()['response'][0]['id']
    else:
        return None


def get_friends(uid: str) -> list:
    url_req = 'https://api.vk.com/method/friends.get'
    params = {'access_token': ACCESS_TOKEN, 'user_id': uid,
              'fields': 'bdate', 'order': 'name', 'v': API_VERSION}
    response = get(url_req, params=params)

    if response.ok:
        return response.json()['response']['items']
    else:
        return None


def count_matching(ages: list, req_age: int) -> int:
    return sum(1 for age in ages if age == req_age)


def get_ages(data: dict) -> list:
    ages = []

    for person in data:
        bdate = person.get('bdate')
        if bdate is not None:
            split_bdate = bdate.split('.')

            if len(split_bdate) == 3:
                ages.append(CURR_YEAR - int(split_bdate[-1]))

    return ages


def get_answer(ages: list) -> list:
    unique = list(set(ages))
    ans = [(age, ages.count(age)) for age in unique]

    return sorted(ans, key=lambda x: (-x[1], x[0]))


def calc_age(uid=None, username=None) -> list:
    if username is not None:
        uid = get_id(username)

    data = get_friends(uid)
    ages = get_ages(data)

    ans = get_answer(ages)

    return ans


if __name__ == '__main__':
    res = calc_age(username='ivaaahn')
    # res = calc_age(username='reigning')
    print(res)
