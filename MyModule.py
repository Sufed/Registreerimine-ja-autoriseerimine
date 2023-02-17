#Registreerimine ja autoriseerimine
import random
def авто_пароль():
    """Генерирует пароль длиной 12 символов"""
    символы='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;!_*-+()/#¤%&'
    salasõna=''.join(random.choice(символы) for _ in range(12)) #Выбирает 12 рандомных символов.
    return salasõna




def проверка_пароля(пароль):
    if any(c.islower() for c in пароль) and any(c.isupper() for c in пароль) and any(c.isdigit() for c in пароль) and any(c in '.,:;!_*-+()/#¤%&' for c in пароль):
        #any - это функция которая присваивает статус True если оно имеется, а если нет то False
        print("Пароль подходит")
    else:
        print("Пароль не подходит")




def Регистрация(users, passw):
    print("Вы выбрали пройти регистрацию.")
    print("Если вы хотите самостоятельно создать пароль нажмите - 1")
    print("Если вы хотите чтобы пароль создался автоматически нажмите - 2")
    выбор1=int(input("Ваш выбор? "))
    if выбор1==1:
        while True:
            пароль=input("Введите пароль: ")
            логин=input("Введите логин: ")
            if проверка_пароля(пароль):
                passw.append(пароль)
                users.append(логин)
                break
    elif выбор1==2:
        логин=input("Введите логин: ")
        salasõna=авто_пароль()
        passw.append(salasõna)
        print("Ваш пароль: ", salasõna)
        users.append(логин)




def Авторизация(users, passw):
    print("Вы выбрали авторизироваться.")
    login=input("Введите логин: ")
    password=input("Введите пароль: ")
    if login in users and password in passw:
        print("Авторизация прошла успешно.")
    else:
        print("Неверный логин и пароль.")

        
        
        
        
def изменение_имени_пользователя(users, old_name, new_name):
    """Изменяет имя пользователя"""
    if old_name in users:
        index = users.index(old_name)
        users[index] = new_name
        print("Имя пользователя успешно изменено.")
    else:
        print("Пользователь с таким именем не найден.")

        
        
        
        
        
def изменение_пароля(passw, user, old_pass, new_pass):
    """Изменяет пароль пользователя"""
    if user in users and old_pass in passw:
        index = users.index(user)
        passw[index] = new_pass
        print("Пароль пользователя успешно изменен.")
    else:
        print("Неверное имя пользователя или пароль.")

        
        
        
def сброс_пароля(passw, user):
    """Сбрасывает пароль пользователя"""
    if user in users:
        index = users.index(user)
        new_pass = авто_пароль()
        passw[index] = new_pass
        print(f"Новый пароль для пользователя {user}: {new_pass}")
    else:
        print("Пользователь с таким именем не найден.")
