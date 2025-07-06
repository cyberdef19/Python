from assistant_core.utils.input_error import input_error
from assistant_core.entities.address_book import AddressBook
from assistant_core.entities.record import Record

"""
Функція add_contact додає нового користувача в словник
Аргументи:
name: str - ім'я користувача 
phone: str - номер телефона
users: dict - словник користувачів з номерами телефонів

return: str - рядок про успіх додавання користувача
"""

@input_error
def add_contact(name: str = None, phone: str = None, contacts: AddressBook = None):
    record: Record = Record(name=name)
    record.add_phone(phone=phone)
    contacts.add_record(record)
    return "Контакт успішно додано"
    
    
    
