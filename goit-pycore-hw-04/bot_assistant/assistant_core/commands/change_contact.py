"""
Функція change_contact - змінює номер телефона користувача
Аргументи:
name: str - ім'я користувача
phone: str - номер телефона користувача
users: dict - словник користувачів з номерами телефонів

return: str - рядок про успіх зміни даних користувача
"""

def change_contact(name: str, phone: str, users: dict):

    if name == " ":
        print("Ім'я користувача не може бути пустим")
        return
    
    if phone == " ":
        print("Значення телефону не може бути пустим")
        return
    
    if name not in users.keys():
        print("Такого користувача в словнику немає. Скористайтеся іншою командою, аби додати нового користувача!")
        return
    
    users[name] = phone
    return "Контакт змінено"