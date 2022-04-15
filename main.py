import hashlib
import json
import os
from data.de_en_code import decode, encode, key
from datetime import datetime


def menu():
    os.system('cls||clear')
    print('Добро пожаловать в мастер заметок\n')
    choise = input(f"1. Войти в аккаунт\n2. Регистрация\n3. Выйти\n")
    if choise == '1':
        if check_user() == 'Accept':
            sticks()
        else:
            input('Неверный логин или пароль\n')
            menu()
    elif choise == '2':
        check = check_user()
        if check == 'Wrong' or check == 'Accept':
            input('Пользователь с таким именем уже существует\n')
            menu()
        elif check == 'new_user':
            sticks()
    elif choise == '3':
        return
    else:
        menu()


def registration():
    os.system('cls||clear')
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    return username, password


def uncode_pass(password: str, data_password: str):
    return True if hashlib.sha256(password.encode()).hexdigest() == data_password else False


def check_user():
    os.system('cls||clear')
    global data_user
    data_user = registration()
    with open('data/data.txt', encoding='utf-8') as file:
        data = file.readlines()
    for i in data:
        if data_user[0] == i.split()[0] and uncode_pass(data_user[1], i.split()[1]):
            return 'Accept'
        elif data_user[0] == i.split()[0] and not uncode_pass(data_user[1], i.split()[1]):
            return 'Wrong'



    with open('data/data.txt', 'a', encoding='utf-8') as file:
        password_decode = hashlib.sha256(data_user[1].encode()).hexdigest()
        file.write(f"{data_user[0]} {password_decode}\n")
    return 'new_user'


def sticks():
    os.system('cls||clear')
    global data
    with open('data/data_sticks.json', encoding='utf-8') as file:
        data = json.load(file)
    print(f'Добро пожаловать, {data_user[0]}\n')
    print('Заметки')
    choise = input(f"1. Создать заметку\n2. Просмотр заметок\n3. Назад\n")
    if choise == '1':
        add_sticks()
    elif choise == '2':
        show_sticks()
    elif choise == '3':
        menu()
    else:
        sticks()


def add_sticks():
    os.system('cls||clear')
    global stick
    global head_stick
    global data_stick
    print('Создать заметку\n')

    head_stick = input('Название заметки: ')
    zametka = input('Напишите заметку: ')

    now = datetime.now()
    data_stick = now.strftime('%d.%m.%Y')
    stick = decode(f"{data_stick}ewq{head_stick}ewq{zametka}", key)
    new_stick: list = [
        {
            'username': data_user[0],
            'sticks': [stick]
        }
    ]
    if write_stick():
        data.append(new_stick[0])
        write_in_file()
    else:
        write_in_file()
    sticks()


def write_in_file():
    with open('data/data_sticks.json', 'w', encoding='utf-8') as write:
        json.dump(data, write, indent=4, ensure_ascii=False)


def write_stick():
    global data
    for s in range(len(data)):
        for i in data[s].keys():
            if data_user[0] == data[s].get(i):
                for k, value in data[s].items():
                    if k == 'sticks':
                        temp = value
                        temp.append(stick)
                        data[s][k] = temp
                        return False
    return True


def show_sticks():
    os.system('cls||clear')
    pars_data()
    print('Просмотр заметок\n')
    choise = input(f"1. Просмотр заметок с сортировкой по дате\n2. Просмотр заметок с сортировкой по названию\n\
3. Поиск заметок по ключевому слову\n4. Назад\n")
    if choise == '1':
        sort_po_date()
    elif choise == '2':
        sort_po_header()
    elif choise == '3':
        search_sticks_by_word()
    elif choise == '4':
        sticks()
    else:
        show_sticks()


def pars_data():
    global encode_stick
    global encode_sticks_data
    encode_sticks_data = []
    for s in data:
        s: dict
        if s['username'] == data_user[0]:
            for i in s['sticks']:
                encode_stick = encode(i, key).split('ewq')
                encode_sticks_data.append(encode_stick)


def sort_po_date():
    os.system('cls||clear')
    print('Просмотр заметок с сортировкой по дате\n')
    for i in encode_sticks_data:
        print(f"{i[0]}: {i[1]}\n{i[2]}\n")
    if input(f"1. Назад\n") == '1':
        show_sticks()
    else:
        sort_po_date()


def sort_po_header():
    os.system('cls||clear')
    print('Просмотр заметок с сортировкой по названию\n')
    for i in sorted(encode_sticks_data, key=lambda x: x[1]):
        print(f"{i[0]}: {i[1]}\n{i[2]}\n")
    if input(f"1. Назад\n") == '1':
        show_sticks()
    else:
        sort_po_header()


def search_sticks_by_word():
    os.system('cls||clear')
    print('Поиск заметок по ключевому слову\n')
    word = input(f"1. Введите ключевое слово или часть слова: ")
    for a, b, c in encode_sticks_data:
        if word.lower() in b.lower():
            print(f"{a}: {b}\n{c}\n")
    if input(f"2. Назад\n") == '2':
        show_sticks()
    else:
        search_sticks_by_word()


def main():
    menu()


if __name__ == '__main__':
    main()