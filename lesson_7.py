# # Home work of 7 lesson
import os
import shutil

'''
    1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
        |--my_project
           |--settings
           |--mainapp
           |--adminapp
           |--authapp
'''


def create_blank():
    main_folder_name = 'my_project'
    child_folders_name = ['settings', 'mainapp', 'adminapp', 'authapp']

    for folder in child_folders_name:
        path = os.path.join(main_folder_name, folder)
        os.makedirs(path)


'''
    |--my_project
      |--settings
      |  |--__init__.py
      |  |--dev.py
      |  |--prod.py
      |--mainapp
      |  |--__init__.py
      |  |--models.py
      |  |--views.py
      |  |--templates
      |     |--mainapp
      |        |--base.html
      |        |--index.html
      |--authapp
      |  |--__init__.py
      |  |--models.py
      |  |--views.py
      |  |--templates
      |     |--authapp
      |        |--base.html
      |        |--index.html
      
      Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
      Написать скрипт, который собирает все шаблоны в одну папку templates, например:
    |--my_project
       ...
      |--templates
       |   |--mainapp
       |   |  |--base.html
       |   |  |--index.html
       |   |--authapp
       |      |--base.html
       |      |--index.html
'''


def copy_templates2():
    base_folder_path = os.path.abspath('my_project')
    name_folder_templates = 'templates'
    folder_templates_path = os.path.join(base_folder_path, name_folder_templates)

    for folder in os.listdir(base_folder_path):
        local_path = os.path.join(base_folder_path, folder)
        if os.path.isdir(local_path):
            for root, dirs, files in os.walk(local_path):
                if name_folder_templates in root:
                    if len(dirs):
                        s = os.path.join(root, dirs[0])
                        d = os.path.join(folder_templates_path, dirs[0])
                        if not os.path.exists(d):
                            shutil.copytree(s, d)


'''
    Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница 
    размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), 
    размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
    Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
'''


def show_sizes(name_dir):
    db = {}
    path_to_dir = os.path.abspath(name_dir)
    for file in os.listdir(path_to_dir):
        path_to_file = os.path.join(path_to_dir, file)
        if os.path.isfile(path_to_file):
            size = os.stat(path_to_file).st_size
            k = 10
            while True:
                if not bool(size // k):
                    break
                else:
                    k *= 10
            if db.get(k):
                db[k] += 1
            else:
                db[k] = 1
    print(db)


if __name__ == '__main__':
    # task 1
    create_blank()

    # task 3
    copy_templates2()

    # task 4
    show_sizes('some_data')
