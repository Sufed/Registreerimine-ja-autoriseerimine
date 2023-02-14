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

