from assistant_core.commands.add_contact import add_contact
from assistant_core.commands.all_users import all_info
from assistant_core.commands.change_contact import change_contact
from assistant_core.commands.hello_cmd import hello_cmd
from assistant_core.commands.show_phone import show_phone
from assistant_core.utils.parse_input import parse_input
from assistant_core.commands.add_birthday import add_birthday
from assistant_core.commands.birthdays import birthdays
from assistant_core.commands.show_birthday import show_birthday
from assistant_core.entities.address_book import AddressBook
import pathlib


def main():
    
    filename = "address_book.dat"
    path = pathlib.Path(filename)
    if path.exists():
        contacts = AddressBook.deserialize_contacts(filename=filename)
    else:
        contacts = AddressBook()
    
    while True:
        user_input = input("Введіть команду з аргументами: ")
        cmd, *args = parse_input(user_input) 
        try:
            match cmd:
                case "close" | "exit":
                    contacts.serialize_contacts(filename=filename)
                    print("Пока. Закінчуємо роботу програми!")
                    break
                case "hello":
                    print(hello_cmd())
                case "add":
                    name, phone = args
                    print(add_contact(name = name, phone = phone, contacts=contacts))
                case "change":
                    name, phone = args
                    print(change_contact(name = name, phone = phone, contacts=contacts))
                case "all":
                    print(all_info(contacts=contacts))
                case "phone":
                    name = args[0]
                    show_phone(name = name, contacts=contacts)
                case "add-birthday":
                    name, birthday = args
                    print(add_birthday(name=name, birthday=birthday, contacts=contacts))
                case "show-birthday":
                    name = args[0]
                    print(show_birthday(name=name, contacts=contacts))
                case "birthdays":
                    print(birthdays(contacts=contacts))
                case _:
                    print("Такої команди ми ще не придумали")
        except ValueError as ex:
            print(str(ex))
        except BaseException as ex:
            print(str(ex))
                        

if __name__ == "__main__":
  main()

