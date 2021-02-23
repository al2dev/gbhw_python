# Home work of 3 lesson
import random


def start():
    modules = [[getattr(Tasks, 'num_translate'), 'Translate', 'Translate entered number'],
               [getattr(Tasks, 'thesaurus'), 'Thesaurus', '2'],
               [getattr(Tasks, 'get_jokes'), 'Get Jokes', 'Generate and return an array of the number of jokes']]

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

    """
        Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

         * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
         реализовать корректную работу с числительными, начинающимися с заглавной буквы.
    """
    @staticmethod
    def num_translate():
        user_input = input('Число: ')
        symbols = ['O', 'T', 'F', 'S', 'E', 'N']
        numbers = {'one':   'один',
                   'two':   'два',
                   'tree':  'три',
                   'four':  'четыре',
                   'five':  'пять',
                   'six':   'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine':  'девять',
                   'ten':   'десять'}

        if user_input[0] in symbols:
            print(f'{user_input} - {numbers.get(user_input.lower()).title()}')
        else:
            print(f'{user_input} - {numbers.get(user_input)}')

    """
        Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в 
        котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
        
        * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате 
        «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, 
        реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с 
        соответствующей буквы
    """
    @staticmethod
    def thesaurus(*arr):
        arr = list(arr)
        if not arr:
            arr = ['Мурат Ибрагимов',
                   'Иван Иванов',
                   'Катя Дьяко',
                   'Ксюша Володькина',
                   'Маша Немидова',
                   'Вова Васильев',
                   'Вася Пупкин']
        result_dict = dict()

        ''' simple version
        for el in arr:
            if el[0] not in result_dict.keys():
                result_dict[el[0]] = [el]
            else:
                result_dict[el[0]].append(el)
        '''

        for el in arr:
            f_name, l_name = tuple(el.split())
            if l_name[0] not in result_dict.keys():
                result_dict[l_name[0]] = {f_name[0]: [el]}
            else:
                if f_name[0] not in result_dict[l_name[0]].keys():
                    result_dict[l_name[0]][f_name[0]] = [el]
                else:
                    result_dict[l_name[0]][f_name[0]].append(el)

        print(f'Not sorted dict: \n{result_dict}\n')

        sorted_dict = {}
        for k in sorted(result_dict.keys()):
            d = {}
            for kk in sorted(result_dict[k].keys()):
                d[kk] = result_dict[k][kk]
            sorted_dict[k] = d

        print(f'Sorted dict: \n{sorted_dict}')

    """
        Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, 
        взятых из трёх списков:
            nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
            adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
            adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
            
        Усложнение: 
        * Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
         (когда каждое слово можно использовать только в одной шутке)? 
         Сможете ли вы сделать аргументы именованными?
    """
    @staticmethod
    def get_jokes(count: int = 3, repeat: bool = False):
        """
           Generate and return an array of the number of jokes

           :param count: counter for the number of jokes
           :param repeat: permission to repeat words
           :return: Array of jokes
        """
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        tmp_a = nouns.copy()
        tmp_b = adverbs.copy()
        tmp_c = adjectives.copy()

        arr_jokes = []

        for i in range(count):
            a, b, c = (random.choice(tmp_a), random.choice(tmp_b), random.choice(tmp_c))
            if not repeat:
                tmp_a.remove(a)
                tmp_b.remove(b)
                tmp_c.remove(c)
            arr_jokes.append(' '.join([a, b, c]))
        print(arr_jokes)


if __name__ == '__main__':
    start()
