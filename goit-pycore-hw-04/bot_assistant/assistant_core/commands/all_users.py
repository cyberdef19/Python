"""
Функція all_info виводить усі імена користувачів та усі номера телефонів

users: dict - приймає словник користувачів
"""

def all_info(users: dict):
    print("Усі записи словника")
    for name, phone in users.items():
        print(name + ": " + phone)