# Home work of 2 lesson
import re
import random


def start():
    modules = [[getattr(Tasks, 'task1'), 'Type of', 'Show type of result different operations'],
               [getattr(Tasks, 'task2'), 'Change list', 'Change and show weather'],
               [getattr(Tasks, 'task3'), 'Say hello', 'Say hello by name'],
               [getattr(Tasks, 'task4'), 'Cost', 'Show modified cost']]

    print('''Hi, please select the required script module:''')
    while True:
        print('')
        for idx, val in enumerate(modules):
            print(f'{idx + 1:>3} - {val[1]}')
            print(f'{str():>6}{val[2]}')

        print(f'''\t0 - Exit''')

        try:
            user_choice = int(input('>>'))
            if not user_choice:
                print('Goodbye!')
                exit()
            elif user_choice < 0 or user_choice > len(modules):
                print('Please select available identification')
            else:
                print('')
                print(modules[user_choice - 1][1])
                modules[user_choice - 1][0]()
        except ValueError:
            print('Please enter an integer selector')


class Tasks:

    """ 1. Выяснить тип результата выражений:
    15 * 3
    15 / 3
    15 // 2
    15 ** 2
    """

    @staticmethod
    def task1():
        op1 = 15 * 3
        op2 = 15 / 3
        op3 = 15 // 2
        op4 = 15 ** 2
        print(f'{"15 * 3"}  type {type(op1)}')
        print(f'{"15 / 3"}  type {type(op2)}')
        print(f'{"15 // 3"} type {type(op3)}')
        print(f'{"15 ** 3"} type {type(op4)}')

    """Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    
    Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до 
    и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
    
    ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
    
    Сформировать из обработанного списка строку:
    
    в "05" часов "17" минут температура воздуха была "+05" градусов
    
    Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
    Как модифицировать это условие для чисел со знаком?
    Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
    Главное: дополнить числа до двух разрядов нулем!

    *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). 
    Эта задача намного серьезнее, чем может сначала показаться.
    """

    @staticmethod
    def task2():
        lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
        without_space = [0]
        need_add = False

        for idx, val in enumerate(lst):
            pattern = r'([-+])(\d)'
            num = re.findall(pattern, val)

            if num and idx not in without_space:
                exec_elem = lst.pop(idx)
                a, b = num[0]
                mode_elem = a + '0' + b if len(b) < 2 else exec_elem
                lst.insert(idx, mode_elem)
                need_add = True

            elif val.isnumeric() and len(val) < 2:
                exec_elem = lst.pop(idx)
                mode_elem = '0' + exec_elem
                lst.insert(idx, mode_elem)

            if need_add or val.isnumeric() and lst[idx - 1] != '"' and lst[idx + 1] != '"':
                need_add = False

                # Так как пробелы добавляем перед словом
                without_space.extend([idx + 1, idx + 2])

                exec_elem = lst.pop(idx)

                lst.insert(idx, '"')
                lst.insert(idx + 1, exec_elem)
                lst.insert(idx + 2, '"')

        result_str = ''
        for idx, val in enumerate(lst):
            result_str += val if idx in without_space else f' {val}'

        print(lst)
        print(result_str)

    """Дан список, содержащий искажённые данные с должностями и именами сотрудников:
    ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
    Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имен и вывести на экран фразы вида: 
    'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
    Можно ли при этом не создавать новый список?
    """

    @staticmethod
    def task3():
        lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

        for v in lst:
            i = len(v) - 1
            name = ''

            while i > 0:
                if v[i] == ' ':
                    break
                name += v[i]
                i -= 1

            hello = 'Привет, ' + name[:-2:-1].upper() + name[-2::-1].lower() + '!'
            print(hello)

    """Создать вручную список, содержащий цены на товары (10–20 товаров), например: [57.8, 46.51, 97, ...]
    
    Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп 
    (например «5 руб 04 коп»). 
    
    Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек 
    (должно быть 07 коп или 00 коп).  
    
    Вывести цены, отсортированные по возрастанию, новый список не создавать 
    (доказать, что объект списка после сортировки остался тот же).
    
    Создать новый список, содержащий те же цены, но отсортированные по убыванию.
    Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
    """

    @staticmethod
    def task4():
        costs = []

        for v in range(random.randint(10, 20)):
            costs.append(round(random.uniform(1, 99), 2))

        print(costs)

        Tasks.show_price(costs)
        Tasks.show_price(sorted(costs))

        costs_small_to_big = []
        costs_small_to_big.extend(reversed(sorted(costs)))
        print(costs_small_to_big)

        Tasks.show_price(costs_small_to_big[:5])

    @staticmethod
    def show_price(arr):
        print()
        for val in arr:
            rub = int(val)
            cent = int(val % rub * 100)
            rounded_cent = cent if cent > 9 else '0' + str(cent)
            print(f'{rub} руб {rounded_cent} коп')


if __name__ == '__main__':
    start()
