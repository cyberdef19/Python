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
            self.value = value
     
        
        