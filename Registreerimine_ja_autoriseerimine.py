# Registreerimine ja autoriseerimine
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
