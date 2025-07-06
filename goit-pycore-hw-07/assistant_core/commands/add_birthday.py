from assistant_core.utils.input_error import input_error
from assistant_core.entities.address_book import AddressBook
from datetime import datetime 

@input_error
def add_birthday(name: str = None, birthday: str = None, contacts: AddressBook = None) -> None:
    
    contact = contacts.find(name)
    contact.add_birthday(birthday)
    return "Дата народження успішно додана"
    
