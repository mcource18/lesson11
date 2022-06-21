import os
import shutil
import platform
from Victory.victory import play_victory
from Buyer.buyer import start_buyer
current_path = os.path.abspath(os.getcwd())


def create_folder(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def remove_folder(path):
    if not os.path.isdir(path):
        shutil.rmtree(path)

def copy_folder(src,dst):
    shutil.copytree(src, dst, dirs_exist_ok=True)


def show_folder(path, show_file=True, show_dir=True):
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)) and show_file:
            print(name)
        if os.path.isdir(os.path.join(path, name)) and show_dir:
            print(name)


while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        name_folder = input("Введите имя папки или файла для создания ")
        create_folder(os.path.join(current_path,name_folder))
    elif choice == '2':
        name_folder = input("Введите имя папки или файла для удаления ")
        remove_folder(os.path.join(current_path,name_folder))
    elif choice == '3':
        name_folder_src = input("Введите имя папки которую надо скопировать ")
        name_folder_dst = input("Введите имя папки в которую надо скопировать ")
        copy_folder(os.path.join(current_path,name_folder_src), os.path.join(current_path,name_folder_dst))
    elif choice == '4':
        show_folder(current_path,True,True)
    elif choice == '5':
        show_folder(current_path, False, True)
    elif choice == '6':
        show_folder(current_path, True, False)
    elif choice=='7':
        print(platform.platform())
    elif choice == '8':
        print("Created: Max")
    elif choice == '9':
        play_victory()
    elif choice == '10':
        start_buyer()
    elif choice == '11':
        path_dir=input("Введите новый путь для рабочей директории " )
        if os.path.exists(path_dir):
            current_path = path_dir
        else:
            print('Путь введен неверно')
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
