from assistant_core.utils.input_error import input_error

"""
Функція change_contact - змінює номер телефона користувача
Аргументи:
name: str - ім'я користувача
phone: str - номер телефона користувача
users: dict - словник користувачів з номерами телефонів

return: str - рядок про успіх зміни даних користувача
"""

@input_error
def change_contact(name: str = None, phone: str = None, users: dict = None):    
    users[name] = phone
    return "Контакт змінено"