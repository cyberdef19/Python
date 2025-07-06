from assistant_core.commands.add_contact import add_contact
from assistant_core.commands.all_users import all_info
from assistant_core.commands.change_contact import change_contact
from assistant_core.commands.hello_cmd import hello_cmd
from assistant_core.commands.show_phone import show_phone
from assistant_core.utils.parse_input import parse_input
from assistant_core.entities.address_book import AddressBook
from assistant_core.entities.record import Record


def main():
    
    contacts = {}
    
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    """
    Тимчасово заокментована нижня частина, бо реалізація адресної книги в боті
    визначена на наступний крок. 
    """
    
    """ while True:
        user_input = input("Введіть команду з аргументами: ")
        cmd, *args = parse_input(user_input) 
        try:
            match cmd:
                case "close" | "exit":
                    print("Пока. Закінчуємо роботу програми!")
                    break
                case "hello":
                    print(hello_cmd())
                case "add":
                    name, phone = args
                    print(add_contact(name = name, phone = phone, users=contacts))
                case "change":
                    name, phone = args
                    print(change_contact(name = name, phone = phone, users=contacts))
                case "all":
                    print(all_info(users=contacts))
                case "phone":
                    name = args
                    show_phone(name = name, users = contacts)
                case _:
                    print("Такої команди ми ще не придумали")
        except ValueError as ex:
            print(str(ex))
        except BaseException as ex:
            print(str(ex))"""
                        

if __name__ == "__main__":
  main()

