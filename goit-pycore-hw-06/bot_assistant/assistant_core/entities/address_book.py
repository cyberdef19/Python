from collections import UserDict
from assistant_core.entities.record import Record
from datetime import datetime

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
    
    def get_upcoming_birthdays(self) -> list[dict]:

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
            days = diff_date.days%365 - leap_years

            """
            Визначаємо чи потрапляє обрана дата у інтервал в 7 наступних днів
            """

            if days <= 7 and days > 0:
                user = {
                    'name': val,
                    'birthday_congratulation': self.data[val].birthday.get_value
                }
                result_users.append(user)
        return result_users
    
        