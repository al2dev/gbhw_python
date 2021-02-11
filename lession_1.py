# Home work of 1 lesson

def start():
    modules = [[getattr(Tasks, 'task1'), 'duration of duration', 'Convert duration seconds to human readable format'],
               [getattr(Tasks, 'task2'), 'sum of digits', 'Sum of digits, odd numbers from 1 ^ 3 to 1000 ^ 3,'
                                                          ' which are divisible by 7'],
               [getattr(Tasks, 'task3'), 'declension of a word', 'Selection of the end of a word depending on'
                                                                 ' the number']]

    print('''Hi, please select the required script module:''')
    while True:
        print('''\n''')
        for idx, val in enumerate(modules):
            print(f'''    {idx + 1} - {val[1]}\n        {val[2]}''')
        print('''    0 - Exit''')

        try:
            user_choice = int(input())
            if not user_choice:
                print('Goodbye!')
                exit()
            elif user_choice < 0 or user_choice > len(modules):
                print('Please select available identification')
            else:
                modules[user_choice - 1][0]()
        except ValueError:
            print('Please enter an integer selector')


class Tasks:
    @staticmethod
    def task1():
        # Change to display null values
        output_zero = True

        second = 1
        minute = second * 60
        hours = minute * 60
        day = hours * 24
        res = ''

        try:
            duration_remainder = int(input())
            if duration_remainder // day:
                res += f'{duration_remainder // day} дн '
                duration_remainder = duration_remainder - duration_remainder // day * day
                check_zero = True

            if duration_remainder // hours or not output_zero:
                res += f'{duration_remainder // hours} час '
                duration_remainder = duration_remainder - duration_remainder // hours * hours
                check_zero = True

            if duration_remainder // minute or not output_zero:
                res += f'{duration_remainder // minute} мин '
                duration_remainder = duration_remainder - duration_remainder // minute * minute

            res += f'{duration_remainder} сек '
            print(res)
        except ValueError:
            print('Please enter an integer selector')

    @staticmethod
    def task2():
        for n in range(1, 1000):
            n_cube = n ** 3
            remainder = n_cube
            summa = 0
            while True:
                if remainder > 10:
                    summa += remainder % 10
                    remainder = int((remainder - remainder % 10) / 10)
                else:
                    summa += remainder
                    break
            if not summa % 7:
                print(f'''number: {n_cube} sum: {summa}''')

    @staticmethod
    def task3():
        ending_array = [' процент', ' процента', ' процентов']
        try:
            user_percent = input()
            if not int(user_percent) < 1 and not int(user_percent) > 20:
                if user_percent in ['1']:
                    user_percent += ending_array[0]
                elif user_percent in ['2', '3', '4']:
                    user_percent += ending_array[1]
                else:
                    user_percent += ending_array[2]
            else:
                raise ValueError
            print(user_percent)
        except ValueError:
            print('Please enter an available value')


if __name__ == '__main__':
    start()
