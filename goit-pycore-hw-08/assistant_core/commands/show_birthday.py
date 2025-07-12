from assistant_core.entities.address_book import AddressBook

def show_birthday(name: str = None, contacts: AddressBook = None) -> str:
    return contacts.find(name).get_birthday.get_value
