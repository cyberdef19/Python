from assistant_core.entities.field import Field
from datetime import datetime

class Birthday(Field):
    
    def __init__(self, value):
        try:
            oDatetime = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(oDatetime)
        except ValueError:
            raise ValueError("Невалідний формат дати. Спробуйте DD.MM.YYYY")
    