from bs4 import BeautifulSoup as bs
from decimal import Decimal
from requests import get


def convert(amount, cur_from, cur_to, date):
    url = "https://www.cbr.ru/scripts/XML_daily.asp"

    r = get(url, params={'date_req': date})

    soup = bs(r.content, 'xml')


    if cur_from == 'RUR':
        from_in_rub = Decimal(1)
    else:
        code_from = soup.find('CharCode', text=cur_from)
        value_from = Decimal(code_from.find_next_sibling('Value').text.replace(',', '.'))
        nominal_from = Decimal(code_from.find_next_sibling('Nominal').text.replace(',', '.'))
        from_in_rub = value_from / nominal_from


    if cur_to == 'RUR':
        to_in_rub = Decimal(1)
    else:
        code_to = soup.find('CharCode', text=cur_to)
        value_to = Decimal(code_to.find_next_sibling('Value').text.replace(',', '.'))
        nominal_to = Decimal(code_to.find_next_sibling('Nominal').text.replace(',', '.'))
        to_in_rub = value_to / nominal_to


    coef = from_in_rub / to_in_rub

    result = Decimal(amount) * coef

    return result.quantize(Decimal('.0001'))