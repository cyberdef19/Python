from assistant_core.entities.name import Name
from assistant_core.entities.phone import Phone
import re

"""
Клас Record описує сутність запис для телефонної книги

В конструкторі приймає значення імені контакта типу рядок
"""

class Record:
    __pattern = "\d{10}" 
    
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        
        
    """
    Властивість get_name дозволяє повернути значення імені контакта 
    """
    @property
    def get_name(self):
        return self.name.get_value
    
    """
    Властивість get_phones дозволяє повернути список об'єктів номерів телефонів
    """
    @property
    def get_phones(self):
        return self.phones
    
    """
    Магічний метод __str__ повертає рядкове значення 
    для об'єкта, що описує читабельно об'єкт
    """
    def __str__(self):
        return f"Contact name: {self.name},\
        phones {';'.join(p.get_value for p in self.phones)}"
        
    
    def __setitem__(self, phone: str):
        if self.__check_phone(phone):
            self.phone = Phone(phone)
            self.phones.append(phone)
        else:
            print("Не можу додати телефон. Він не валідний")
    
    """
    Метод add_phone для додавання номера телефону
    в список контактів
    
    Аргументи:
    phone: str - номер телефону типу рядок
    
    return: None
    """
        
    def add_phone(self, phone: str) ->None:
        if self.__check_phone(phone):
            self.phone = Phone(phone)
            self.phones.append(self.phone)
        else:
            print("Не можу додати телефон. Він не валідний")
            
    """
    Метод remove_phone для видалення номера телефону
    
    Аргументи:
    phone: str - номер телефона типу рядок
    
    return: str повертає 
    """

    def remove_phone(self, phone: str) -> None:
        try:
            oPhone = Phone(phone)
            self.phones.remove(oPhone)
        except ValueError:
            print("Такого номеру телефона у базі не знайдено")
    
    """
    Метод edit_phone для редагування номера телефону 
    
    Аргументи:
    old_phone: str - старий номер телефона типу рядок
    new_phone: str - новий номер телефона типу рядок
    
    return: None
    """
            
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        index = self.__search_phone(old_phone)
        if index == -1:
            return None
        oPhone = Phone(new_phone)
        self.phones[index] = oPhone
        
    """
    Метод find_phone для пошуку номера телефона у контактах
    
    Аргументи:
    phone: str - номер телефону
    
    return: str - повертає рядок зі значенням знайденого номера телефона
    """
    
    def find_phone(self, phone: str) -> str:
        index = self.__search_phone(phone)
        return self.phones[index].get_value   
    
    """
    Приватний метод __check_phone для перевірки валідності номера телефона
    Має бути рядком з 10 чисел
    
    Аргумент:
    phone: str - номер телефона типу рядок
    
    return: bool - валідний номер чи ні
    """
    
    def __check_phone(self, phone: str) -> bool:
        return bool(re.match(Record.__pattern, phone))
    
    """
    Приватний метод __search_phone для пошуку номера телефона у контактах
    
    Аргументи:
    phone: str - рядок зі значенням номера телефона
    
    return: int - повертає індекс контакту знайденого телефона
    """
    
    def __search_phone(self, phone: str) -> int:
        try:
            oPhone = Phone(phone)
            return self.phones.index(oPhone)
        except ValueError:
            print("Такого номера телефону не знайдено!")
            return -1


    