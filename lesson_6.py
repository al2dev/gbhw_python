# Home work of 6 lesson
from requests import get
from itertools import islice
from itertools import zip_longest

# global variable <'ip: str': query: int>
clients = {}


# Methods for 1 tasks

def download_log(url):
    local_filename = f"{url.split('/')[-1]}.txt"
    with get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def get_clients_query(file):
    return [get_data(line) for line in file]


def get_data(line):
    global clients
    str_line = line.replace('"', '')
    arr_line = str_line.split()
    ip, method, path = arr_line[0], arr_line[5], arr_line[6]
    if ip in clients:
        clients[ip] += 1
    else:
        clients[ip] = 1
    return ip, method, path


# Methods for 2 task

def get_spamer(file):
    get_clients_query(file)
    sorted_clients = sorted(clients.items(), key=lambda item: item[1], reverse=True)
    for ip, query in sorted_clients:
        yield ip, query


# Methods for 3 task

def create_test_files(users_filename, hobbies_filename):
    users = '''Иванов,Иван,Иванович\nПетров,Петр,Петрович\nМаксимов,Максим,Максимыч'''
    hobbies = '''скалолазание,охота\nгорные лыжи'''

    file_user = open(users_filename, 'w')
    file_hobby = open(hobbies_filename, 'w')

    file_user.write(users)
    file_hobby.write(hobbies)

    file_user.close()
    file_hobby.close()


def create_end_file(users_filename, hobbies_filename):
    file_user = open(users_filename, 'r')
    file_hobby = open(hobbies_filename, 'r')

    result = {key: val for key, val in zip_longest(file_user, file_hobby, fillvalue=None) if key is not None}
    print(result)

    end_file = open('users_hobby.csv', 'w')
    end_file.write(str(result)
                   .replace('{', '')
                   .replace('}', '')
                   .replace('\'', '')
                   .replace('\\n', '')
                   .replace(', ', '\n'))

    end_file.close()
    file_user.close()
    file_hobby.close()


if __name__ == '__main__':

    # download logs
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    logs_filename = download_log(url)
    print(logs_filename)

    # open file
    logs_file = open(logs_filename, 'r')

    '''
        Не используя библиотеки для парсинга, распарсить  файл логов web-сервера nginx_logs.txt
        — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
    '''
    # 1 task
    print('\n1 task')
    clients_query = get_clients_query(logs_file)
    print(clients_query[:20])

    '''
        Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания. 
        Спамер — это клиент, отправивший больше всех запросов; 
        код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
    '''
    # 2 task
    print('\n2 task')
    show_bad_guys = 5
    spam = get_spamer(logs_file)
    print(*islice(spam, show_bad_guys))

    # close file
    logs_file.close()

    '''
        Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
        Известно, что при хранении данных используется принцип: одна строка — один пользователь, 
        разделитель между значениями — запятая. 
        Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
        ключи — ФИО, значения — данные о хобби. 
        Сохранить словарь в файл.
    '''

    # 3 task
    print('\n3 task')
    users_filename = 'users.csv'
    hobbies_filename = 'hobby.csv'
    create_test_files(users_filename, hobbies_filename)
    create_end_file(users_filename, hobbies_filename)
