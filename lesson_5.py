# Home work of 5 lesson
from itertools import islice


''' 1
    Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
    полностью истощить генератор.
'''


def iterator_without_yield(max_num):
    if max_num ** 2 > 200:
        return None
    return (num for num in range(1, max_num + 1, 2))


''' 2
     Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. 
     Полностью истощить генератор.
        Усложнение(*):
        С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), 
        для чисел, квадрат которых меньше 200.
        
        Усложнение(**):
        С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел. 
'''


def iterator_with_yield(max_num):
    if max_num ** 2 > 200:
        return None
    amount = 0
    for num in range(1, max_num + 1, 2):
        amount += num
        yield num, amount


''' 3
    Есть два списка:
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей', 
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
    
    ('Иван', '9А')
    ('Анастасия', '7В')
    ...
    
    Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, 
    чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
    
    ('Станислав', None)
    
    Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях 
    генератор даст эффект.
'''


def tutors_classes(tut, kl):
    for num in range(0, len(tut)):
        c = kl[num] if num < len(kl) else None
        yield tut[num], c


''' 4
    Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]
    Выводит или не выводить первый элемент - решите сами. Используйте генераторы или генераторные выражения.
    Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
'''


def bigger(arr):
    return [num_2 for num_1, num_2 in zip(arr, arr[1:]) if num_2 > num_1]


''' 5
    Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список 
    с сохранением порядка их следования в исходном списке, например:
        src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
        result = [23, 1, 3, 10, 4, 11]
    Используйте генераторы или генераторные выражения.
    Сначала найдите способ определить уникальность элемента в списке. Подумайте о сохранении порядка исходного списка.
'''


def liquidation_clone(arr):
    return [num for idx, num in enumerate(arr) if num not in arr[:idx] and num not in arr[idx+1:]]


if __name__ == '__main__':
    num = 11

    # 1 task
    print('\n1 task')
    gen1 = iterator_without_yield(num)
    print(*islice(gen1, num))

    # 2 task
    print('\n2 task')
    gen2 = iterator_with_yield(num)
    print(*islice(gen2, num))

    # 3 task
    print('\n3 task')
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В']
    res_tutors_classes = tutors_classes(tutors, klasses)
    print(*res_tutors_classes)

    # 4 task
    print('\n4 task')
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    res_bigger = bigger(src)
    print(res_bigger)

    # 5 task
    print('\n5 task')
    clones = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    res_liquidation_clone = liquidation_clone(clones)
    print(clones, res_liquidation_clone)
