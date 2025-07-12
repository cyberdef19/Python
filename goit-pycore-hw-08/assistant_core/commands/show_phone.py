from assistant_core.utils.input_error import input_error
from assistant_core.entities.address_book import AddressBook
from assistant_core.entities.record import Record
"""
Функція show_phone - виводить номер телефона заданого користувача

name: str - ім'я користувача
users: dict - словник з користувачів

return: str - повертає рядок, що сповіщує про успішне виконання операції
"""

@input_error
def show_phone(name: str = None, contacts: AddressBook = None):
    contact = contacts.find(name=name)
    for phone in contact.phones:
        print(phone)
    return "Успішно перелічено усі номери телефонів юзерів"
    