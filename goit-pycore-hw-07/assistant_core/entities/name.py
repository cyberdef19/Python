from assistant_core.entities.field import Field

"""
 Класс, що реалізує поле name
 Успадковує клас Field 
 
 В конструкторі приймає значення аргументу value типу any
 та передає його в батьківський клас
"""

class Name(Field):
    
    def __init__(self, value):
        super().__init__(value)