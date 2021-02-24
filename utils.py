from requests import get, utils
from datetime import date


def currency_rates(argv):
    if type(argv) == list:
        programm, valute = argv
    else:
        valute = argv

    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    enc = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(enc)

    # Get date
    date_find = 'Date="'
    date_pos = content.find(date_find)
    date_len = len('2020.20.20')
    date_str = content[date_pos + len(date_find): date_pos + len(date_find) + date_len]
    date_arr = date_str.split('.')
    date_obj = date(int(date_arr[2]), int(date_arr[1]), int(date_arr[0]))

    # Get value valute
    valute_find = valute.upper()
    tag_start = '<Value>'
    tag_stop = '</Value>'
    valute_pos = content.find(valute_find)
    if valute_pos < 0:
        return None
    value_start = content[valute_pos:].find(tag_start) + len(tag_start)
    value_stop = content[valute_pos:].find(tag_stop)
    valute_value = float(content[valute_pos + value_start: valute_pos + value_stop].replace(',', '.'))

    return valute_value, date_obj


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))
