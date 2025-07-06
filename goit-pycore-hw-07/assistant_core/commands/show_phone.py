from assistant_core.utils.input_error import input_error

"""
Функція show_phone - виводить номер телефона заданого користувача

name: str - ім'я користувача
users: dict - словник з користувачів

return: str - повертає рядок, що сповіщує про успішне виконання операції
"""

@input_error
def show_phone(name: str = None, users: dict = None):
    if name in users.keys():
        print("Номер телефону " + name + ": " + users[name])
    else:
        print("Немає такого користувача в системі")
    return "Успішно перелічено усі номери телефонів юзерів"
    