"""
Функція show_phone - виводить номер телефона заданого користувача

name: str - ім'я користувача
users: dict - словник з користувачів

return: -
"""

def show_phone(name: str, users: dict):
    if name in users.keys():
        print("Номер телефону " + name + ": " + users[name])
    else:
        print("Немає такого користувача в системі")