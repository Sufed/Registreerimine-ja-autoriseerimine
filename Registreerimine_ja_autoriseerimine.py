# Registreerimine ja autoriseerimine
from MyModule import *

users=["user1", "user2"]
passw=["12345", "qwerty"]

while True:
    print("Если вы хотите пройти регистрацию нажмите - 1")
    print("Если вы хотите авторизироваться нажмите - 2")
    print("Если вы хотите изменить имя пользователя нажмите - 3")
    print("Если вы хотите изменить пароль нажмите - 4")
    print("Если вы забыли свой пароль нажмите - 5")
    print("Если вы хотите закончить работу нажмите - 6")
    выбор = int(input("Ваш выбор? "))

    if выбор == 1:
        Регистрация(users, passw)
    elif выбор == 2:
        Авторизация(users, passw)
    elif выбор == 3:
        old_username = input("Введите текущее имя пользователя: ")
        new_username = input("Введите новое имя пользователя: ")
        change_username(users, old_username, new_username)
    elif выбор == 4:
        username = input("Введите имя пользователя: ")
        old_password = input("Введите старый пароль: ")
        new_password = input("Введите новый пароль: ")
        change_password(users, passw, username, old_password, new_password)
    elif выбор == 5:
        username = input("Введите имя пользователя: ")
        reset_password(users, passw, username)
    elif выбор == 6:
        print("Вы выбрали закончить работу.")
        break

'''# Registreerimine ja autoriseerimine
import MyModule

users=["user1", "user2"]
passw=["12345", "qwerty"]

while True:
    print("Если вы хотите пройти регистрацию нажмите - 1")
    print("Если вы хотите авторизироваться нажмите - 2")
    print("Если вы хотите закончить работу нажмите - 3")
    выбор=int(input("Ваш выбор? "))

    if выбор==1:  # Регистрация
        print("Вы выбрали пройти регистрацию.")
        print("Если вы хотите самостоятельно создать пароль нажмите - 1")
        print("Если вы хотите чтобы пароль создался автоматически нажмите - 2")
        выбор1 = int(input("Ваш выбор? "))
        if выбор1==1:
            while True:
                пароль = input("Введите пароль: ")
                логин = input("Введите логин: ")
                if MyModule.проверка_пароля(пароль):
                    passw.append(пароль)
                    users.append(логин)
                    break
        elif выбор1==2:
            логин = input("Введите логин: ")
            salasõna = MyModule.авто_пароль()
            passw.append(salasõna)
            print("Ваш пароль: ", salasõna)
            users.append(логин)


    elif выбор==2:  # Авторизация
        print("Вы выбрали авторизироваться.")
        login=input("Введите логин: ")
        salasõna=input("Введите пароль: ")
        if login in users and salasõna in passw:
            print("Авторизация прошла успешно.")
        else:
            print("Неверный логин и пароль.")



    elif выбор==3:  # Выход
        print("Вы выбрали закончить работу.")
        break
'''
