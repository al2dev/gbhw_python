from utils import currency_rates

if __name__ == '__main__':
    codes = ['USD', 'BYN', 'CNY', 'JPY', 'TRY', 'NSV']

    for code in codes:
        print(currency_rates(code))
