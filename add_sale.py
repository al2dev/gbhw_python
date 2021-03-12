from sys import argv


bakery_filename = 'bakery.csv'

if __name__ == '__main__':
    bakery_file = open(bakery_filename, 'a+', encoding='utf-8')
    print('Ready to add')

    if len(argv) < 2:
        print('Please enter number')
    elif len(argv) == 2:
        bakery_file.write(str(argv[1]) + '\n')
        print('Was added:', argv[1])
    elif len(argv) == 3:
        print("Doesn't support many args, enter one number")

    bakery_file.close()
