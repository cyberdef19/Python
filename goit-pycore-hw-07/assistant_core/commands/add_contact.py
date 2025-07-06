from assistant_core.utils.input_error import input_error

"""
Функція add_contact додає нового користувача в словник
Аргументи:
name: str - ім'я користувача 
phone: str - номер телефона
users: dict - словник користувачів з номерами телефонів

return: str - рядок про успіх додавання користувача
"""

@input_error
def add_contact(name: str = None, phone: str = None, users: dict = None):
    users[name] = phone
    return "Contact added"
    
    
    
