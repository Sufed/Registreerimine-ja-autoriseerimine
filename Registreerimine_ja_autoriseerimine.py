# Registreerimine ja autoriseerimine
from MyModule import *

users=["user1", "user2"]
passw=["12345", "qwerty"]

while True:
    print("Kui soovite registreeruda, vajutage - 1")
    print("Kui soovite sisse logida, vajutage - 2")
    print("Kui soovite muuta kasutajanime, vajutage - 3")
    print("Kui soovite salasõna muuta, vajutage - 4")
    print("Kui soovite salasõna lähtestada, vajutage - 5")
    print("Kui soovite töö lõpetada, vajutage - 6")
    выбор = int(input("Teie valik? "))

    if выбор == 1:
        Регистрация(users, passw)
    elif выбор == 2:
        Авторизация(users, passw)
    elif выбор == 3:
        старыйлогин = input("Sisestage praegune kasutajanimi: ")
        новыйлогин = input("Sisestage uus kasutajanimi: ")
        изменение_имени_пользователя(users, старыйлогин, новыйлогин)
    elif выбор == 4:
        логин = input("Sisestage oma kasutajanimi: ")
        старыйпароль = input("Sisestage vana parool: ")
        новыйпароль = input("Sisestage uus parool: ")
        изменение_пароля(users, passw, логин, старыйпароль, новыйпароль)
    elif выбор ==5:
        логин= input("Sisestage oma kasutajanimi: ")
        сброс_пароля(passw, логин, users)
    elif выбор == 6:
        print("Te olete otsustanud töö lõpetada.")
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
