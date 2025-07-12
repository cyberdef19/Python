from collections import UserDict
from assistant_core.entities.record import Record
from datetime import datetime
import pickle

"""
Клас AddressBook спадкоємець скласа UserDict

"""

class AddressBook(UserDict):
    
    """
    Функція serialize_contacts серіалізує стан об'єкта self
    зберігаючи його дані у файл address_book.dat
    
    Аргументи:
    filename: str - шлях до файлу у вигляді рядка
    
    """
    
    def serialize_contacts(self, filename: str) -> None:
        with open(filename, "wb") as f:
            pickle.dump(self, f)
    
    """
    Метод deserialize_contacts - статичний метод для десеріалізації об'єкта 
    з файла address_book.dat. Метод є статичним, бо не залежить від стану 
    об'єкта та не залежить від змінних класу і об'єкта, але повертає
    десеріалізований об'єкт книги контактів
    
    Аргументи:
    filename: str - шлях до файлу з серіалізованим об'єктом
    
    return: AddressBook  - повертає об'єкт типу AddressBook
    """
    
    @staticmethod
    def deserialize_contacts(filename: str):
        try:
            with open(filename, "rb") as f:
                contacts = pickle.load(f)
        except FileNotFoundError as ex:
            print(str(ex))
            return []
        return contacts
    
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
    
    def get_upcoming_birthdays(self) -> None:

        result_users = []
        
        """
        Отримаємо сьогоднішню дату
        """
        today_date = datetime.today().date()

        """


        Отримуємо об'єкт datetime для дати з users 
        і визначимо які співробітники мають шанс отримати поздоровлення в наступні 7 днів
        Визначимо також кількість високосних літ між датою дня народження та сьогоднішньою датою
        Отримаємо об'єкт типу deltatime, визначивши кількість днів між датою народження та сьогоднішньою датою
        Поділемо кількість отриманих днів за моделум на 365 днів і визначимо скільки реальних днів 
        між сьогоднішнім числом та датою народження, віднявши також у якості поправки кількість 
        днів, що додалися за високосні роки
        """
        
        for val in self.keys():
            birthday = self.data[val].birthday.get_value.date()
            diff_years = today_date.year - birthday.year
            leap_years = round(diff_years/4) 
            diff_date = today_date - birthday
            days = abs(diff_date.days%365 - leap_years)

            """
            Визначаємо чи потрапляє обрана дата у інтервал в 7 наступних днів
            """

            if days <= 7 and days > 0:
                print(val + ":  " + str(self.data[val].birthday.get_value))
               
        
        