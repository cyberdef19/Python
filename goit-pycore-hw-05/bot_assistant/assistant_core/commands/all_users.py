from assistant_core.utils.input_error import input_error

"""
Функція all_info виводить усі імена користувачів та усі номера телефонів

users: dict - приймає словник користувачів

return: str - рядок про успіх виведення інформації
"""

@input_error
def all_info(users: dict = None):
    print("Усі записи словника")
    for name, phone in users.items():
        print(name + ": " + phone)
    return "Успішний вивід інформації"