

'''
    Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
'''


class Date:
    def __init__(self, user_date):
        self.user_date = user_date

    @classmethod
    def date_execute(cls, user_date):
        return list(map(int, user_date.split('-')))

    @staticmethod
    def date_validate(user_date):
        try:
            arr_date = Date.date_execute(user_date)
            if arr_date[2] % 4 or not arr_date[2] % 100 and arr_date[2] % 400:
                if arr_date[0] in range(1, 32) and arr_date[1] in [1, 3, 5, 7, 8, 10, 12] \
                        or arr_date[0] in range(1, 31) and arr_date[1] in [4, 6, 9, 11] \
                        or arr_date[0] in range(1, 29) and arr_date[1] in [2]:
                    return True
                else:
                    return False
            else:
                if arr_date[0] in range(1, 32) and arr_date[1] in [1, 3, 5, 7, 8, 10, 12] \
                        or arr_date[0] in range(1, 31) and arr_date[1] in [4, 6, 9, 11] \
                        or arr_date[0] in range(1, 30) and arr_date[1] in [2]:
                    return True
                else:
                    return False
        except IndexError:
            return False
        except ValueError:
            return False


'''
    оздайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
    Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа 
    должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class OwnZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def try_division():
    while True:
        a = input('enter a: ')
        if a == 'stop':
            break
        b = input('enter b: ')
        try:
            if int(b) == 0:
                raise OwnZero('Деление на 0 недопустимо')
            print(int(a) / int(b))
        except OwnZero as err:
            print(err)
        finally:
            print('try again')


'''
    Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
    Проверить работу исключения на реальном примере. 
    Запрашивать у пользователя данные и заполнять список необходимо только числами. 
    Класс-исключение должен контролировать типы данных элементов списка.
'''


class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_numbers(st):
    try:
        int(st)
        return True
    except ValueError:
        raise NotNumber('Вводите только числа!')


def enter_numbers():
    arr = []
    while True:
        i = input('enter number: ')
        if i == 'stop':
            break
        else:
            try:
                check_numbers(i)
                arr.append(int(i))
            except NotNumber as err:
                print(err)
            finally:
                print('next number..')
    print(arr)


if __name__ == '__main__':
    # 1 task
    print('\n')
    print('Task 1')

    print(Date.date_execute('29-02-2021'))
    print(Date.date_execute('23-14-2021'))

    print(Date.date_validate('29-02-2020'))
    print(Date.date_validate('29-02-2021'))
    print(Date.date_validate('23-14-2021'))
    print(Date.date_validate('7-12-1917'))
    print(Date.date_validate('29/02/2020'))

    # 2 task
    print('\n')
    print('Task 2')
    try_division()

    # 3 task
    print('\n')
    print('Task 3')
    enter_numbers()
