from collections import UserDict
from assistant_core.entities.record import Record


"""
Клас AddressBook спадкоємець скласа UserDict

"""

class AddressBook(UserDict):
    
    """
    Метод aad_record додає запис до книги контактів
    
    Аргументи:
    record: Record об'єкт що представляє собою запис типу Record
    
    return: None
    """
    
    def add_record(self, record: Record)-> None:
        self.data[record.get_name] = record
    
    
    """
    Метод для пошуку контакта за ключем у вигляді імені типу рядок
    
    Аргумент: 
    name: str - ім'я контакта типу рядок
    return: Record  - повертає запис
    """
    def find(self, name: str) -> Record:
        if name in self.keys():
            return self.data[name]
        else:
            print("Такого ключа не знайдено")
            return None
    
    """
    Метод delete для видалення запису зі списку контактів
    
    Аргументи:
    name: str - ім'я контакта типу рядок
    
    return: None
    """
    
    def delete(self, name: str) -> None:
        if name in self.keys():
            self.pop(name)
        else:
            print("Немає такого ключа")
    
    
    
        