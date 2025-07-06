from assistant_core.entities.phone import Phone
from assistant_core.entities.birthday import Birthday
from datetime import datetime
import re

"""
Клас Field визначає поле для запису книги телефонів

В конструкторі приймає значення value: any
"""

class Field:
    pattern_phone = "\d{10}"
    
    def __init__(self, value: any):
        self.value = value

    """
    Магічний метод __str__ повертає рядкове значення 
    для об'єкта, що описує читабельно об'єкт
    """
    
    def __str__(self):
        return str(self.value)
    
    """
    Властивість get_value повертає значення 
    поля value
    """
    @property
    def get_value(self) -> any:
        return self.value
    
    """
    Властивість set_value встановлює значення
    для поля value
    """
    
    @get_value.setter
    def set_value(self, value: any) -> None:
        try:
            if isinstance(value, Phone):
                re.match(Field.get_value, value)
            if isinstance(value, datetime):
                datetime.strptime(value, "%d.%M.Y")
            self.value = value
        except ValueError:
            raise ValueError("Не валідне значення поля")
        
        