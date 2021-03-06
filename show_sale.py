from sys import argv


bakery_filename = 'bakery.csv'

if __name__ == '__main__':
    bakery_file = open(bakery_filename, 'r', encoding='utf-8')
    bakery_file.seek(0)
    print('Ready to show')

    if len(argv) < 2:
        print(bakery_file.read())

    elif len(argv) == 2:
        gen = [line for idx, line in enumerate(bakery_file.readlines()) if idx + 2 > int(argv[1])]
        print(gen)

    elif len(argv) == 3:
        gen = [line for idx, line in enumerate(bakery_file.readlines()) if idx + 2 > int(argv[1]) and idx < int(argv[2])]
        print(gen)

    bakery_file.close()
