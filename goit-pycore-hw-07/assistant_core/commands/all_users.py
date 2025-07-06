from assistant_core.utils.input_error import input_error
from assistant_core.entities.address_book import AddressBook

"""
Функція all_info виводить усі імена користувачів та усі номера телефонів

users: dict - приймає словник користувачів

return: str - рядок про успіх виведення інформації
"""

@input_error
def all_info(contacts: AddressBook = None):
    print("Усі записи словника")
    for name, record in contacts.data.items():
        print(record)
    return "Успішний вивід інформації"