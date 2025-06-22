"""
Функція add_contact додає нового користувача в словник
Аргументи:
name: str - ім'я користувача 
phone: str - номер телефона
users: dict - словник користувачів з номерами телефонів

return: - 
"""

def add_contact(name: str, phone: str, users: dict):

    if name == " ":
        print("Ім'я користувача не може бути пустим")
        return
    
    if phone == " ":
        print("Значення телефону не може бути пустим")
        return
    
    if name in users.keys():
        print("Таке ім'я в базі вже є. Оберіть іншу функцію - функцію заміни номера телефону")
        return

    users[name] = phone
    print("Contact added")
    
    
    
