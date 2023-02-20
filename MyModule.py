#Registreerimine ja autoriseerimine
import random
def авто_пароль():
    """Генерирует пароль длиной 12 символов"""
    символы='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;!_*-+()/#¤%&'
    salasõna=''.join(random.choice(символы) for _ in range(12)) #Выбирает 12 рандомных символов.
    return salasõna



def проверка_пароля(пароль):
    """Проверка пароля"""
    if any(c.islower() for c in пароль) and any(c.isupper() for c in пароль) and any(c.isdigit() for c in пароль) and any(c in '.,:;!_*-+()/#¤%&' for c in пароль):
        #any - это функция которая присваивает статус True если оно имеется, а если нет то False
        print("Parool sobib")
    else:
        print("Parool ei sobi")



def Регистрация(users, passw):
    """Регистрация"""
    print("Te olete otsustanud registreeruda.")
    print("Kui soovite ise salasõna luua, vajutage - 1")
    print("Kui soovite, et parool loodaks automaatselt, vajutage - 2")
    выбор1=int(input("Teie valik? "))
    if выбор1==1:
        while True:
            пароль=input("Sisestage oma parool: ")
            логин=input("Sisestage oma kasutajanimi: ")
            if проверка_пароля(пароль):
                passw.append(пароль)
                users.append(логин)
                break
    elif выбор1==2:
        логин=input("Sisestage oma kasutajanimi: ")
        salasõna=авто_пароль()
        passw.append(salasõna)
        print("oma parool: ", salasõna)
        users.append(логин)




def Авторизация(users, passw):
    """Авторизация"""
    print("Olete valinud sisselogimise.")
    login=input("Sisestage oma kasutajanimi: ")
    password=input("Sisestage oma parool: ")
    if login in users and password in passw:
        print("Loa andmine oli edukas.")
    else:
        print("Vale sisselogimine ja salasõna.")

        
        
        
        
def изменение_имени_пользователя(users, старыйлогин, новыйлогин):
    """Изменяет имя пользователя"""
    if старыйлогин in users:
        index = users.index(старыйлогин)
        users[index] = новыйлогин
        print("Kasutajanimi on edukalt muudetud.")
    else:
        print("Selle nimega kasutajat ei leitud.")

        
        
        
        
        
def изменение_пароля(users, passw, логин, старыйпароль, новыйпароль):
    """Изменяет пароль пользователя"""
    if логин in users and старыйпароль in passw: #Дать выбор старого пароля
        index = users.index(логин)
        passw[index] = новыйпароль
        print(f"Kasutaja parool on edukalt muudetud. Vana parool - {старыйпароль}")
    else:
        print("Vale kasutajanimi või salasõna.")

        
        
        
def сброс_пароля(passw, логин, users):
    """Сбрасывает пароль пользователя"""
    if логин in users: #Проверяется есть ли логин в списке пользователей
        index = users.index(логин) #Смотрит индекс логина.
        выбор2 = int(input("Kui soovite säilitada vana salasõna, vajutage - 1. Kui soovite uut, vajutage 2: "))
        if выбор2 == 1:
            print(f"Kasutaja vana parool {логин}: {passw[index]}.")
        elif выбор2 == 2:
            новыйпароль = авто_пароль()
            passw[index] = новыйпароль
            print(f"Kasutaja uus parool {логин}: {новыйпароль}.")
            print(passw)
    else:
        print("Selle nimega kasutajat ei leitud.")
