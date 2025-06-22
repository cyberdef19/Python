from assistant_core.commands.add_contact import add_contact
from assistant_core.commands.all_users import all_info
from assistant_core.commands.change_contact import change_contact
from assistant_core.commands.hello_cmd import hello_cmd
from assistant_core.commands.show_phone import show_phone
from assistant_core.utils.parse_input import parse_input

if __name__ == "__main__":

    contacts = {}

    while True:
        user_input = input("Введіть команду з аргументами: ")
        cmd, *args = parse_input(user_input) 
        try:
            match cmd:
                case "close" | "exit":
                    print("Пока. Закінчуємо роботу програми!")
                    break
                case "hello":
                    hello_cmd()
                case "add":
                    name, phone = args
                    add_contact(name, phone, contacts)
                case "change":
                    name, phone = args
                    change_contact(name, phone, contacts)
                case "all":
                    all_info(contacts)
                case "phone":
                    name = args
                    show_phone(name, contacts)
                case _:
                    print("Такої команди ми ще не придумали")
        except ValueError as ex:
            print(str(ex))
        except BaseException as ex:
            print(str(ex))
                    

