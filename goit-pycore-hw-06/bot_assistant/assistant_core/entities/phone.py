from assistant_core.entities.field import Field
"""
Клас phone успадковує клас Field та визначає 
поле номер телефона.

У конструкторі приймає рядок з номером телефона
передає його батьківський клас     
"""

class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        
    """
    Магічний метод __eq__ для порівняння об'єктів типу Phone
    """
    
    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False
    