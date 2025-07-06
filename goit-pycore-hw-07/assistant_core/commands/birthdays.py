from assistant_core.entities.address_book import AddressBook

def birthdays(contacts: AddressBook = None) -> list[dict]:
    contacts.get_upcoming_birthdays()
    return "Дати народження успішно відображено"
    
