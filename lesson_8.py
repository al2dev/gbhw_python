import re


"""
    Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
     и почтовый домен из email адреса и возвращает их в виде словаря. 
    Если адрес не валиден, выбросить исключение ValueError.
"""


def email_parse(email_address):
    RE_EMAIL = re.compile(r'(?P<name>\w+|(\w+(.|-|_)\w+){1,10})[@](?P<domain>\w+\.\w{2,6})')
    res = RE_EMAIL.search(email_address)
    if res:
        return {'name': res.group('name'), 'domain': res.group('domain')}
    else:
        raise ValueError('Email not found')


"""
     Написать декоратор для логирования типов позиционных аргументов функции

     * Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
      и выбрасывать исключение ValueError, если что-то не так
"""


def val_checker(func):
    res = func.__name__

    def get_wrapper(*args):
        if len(args):
            markups = []
            types = []
            for el in args:
                if el > 0:
                    markups.append(func(el))
                    types.append(f'{res}({el}: {type(el)})')
                else:
                    raise ValueError(f'wrong val {el}')
            print(types)
            return markups
        else:
            raise ValueError(f'wrong val {args}')
    return get_wrapper


@val_checker
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    # task 1
    print(email_parse('someone@geekbrains.ru')) # ok
    print(email_parse('elvin_85@gmail.com')) # ok
    print(email_parse('someone@geekbrainsru')) # exception
    print(email_parse('example@gmail_com')) # exception
    print(email_parse('79996541234@yandex.com')) # ok

    # task 3, 4
    print(calc_cube(3))
    print(calc_cube(3, 5, 7))
    print(calc_cube(9, -3))
    print(calc_cube(-1))
    print(calc_cube())
