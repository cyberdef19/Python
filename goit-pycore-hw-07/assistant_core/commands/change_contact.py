from assistant_core.utils.input_error import input_error
from assistant_core.entities.address_book import AddressBook
from assistant_core.entities.record import Record

"""
Функція change_contact - змінює номер телефона користувача
Аргументи:
name: str - ім'я користувача
phone: str - номер телефона користувача
users: dict - словник користувачів з номерами телефонів

return: str - рядок про успіх зміни даних користувача
"""

@input_error
def change_contact(name: str = None, phone: str = None, contacts: AddressBook = None):    
    record: Record = Record(name=name)
    record.add_phone(phone=phone)
    contacts.add_record(record)
    return "Контакт змінено"