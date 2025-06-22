"""
Функція all_info виводить усі імена користувачів та усі номера телефонів

users: dict - приймає словник користувачів

return: str - рядок про успіх виведення інформації
"""

def all_info(users: dict):
    print("Усі записи словника")
    for name, phone in users.items():
        print(name + ": " + phone)
    return "Успішний вивід інформації"