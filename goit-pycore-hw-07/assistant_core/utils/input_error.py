import re

"""
Декоратор input_error - фільтрує помилковий користувацький ввід даних
з метою не навантажувати обробкою помилок самі функції

"""


def input_error(func):
    
    """
    Визначимо паттерни регулярних виразів для імені користувача і номера телефона
    """
    pattern_name = r"^[A-ZА-ЯІЇЄҐ][a-zа-яіїєґ']+(-[A-ZА-ЯІЇЄҐ]?[a-zа-яіїєґ']+)*(\s[A-ZА-ЯІЇЄҐ][a-zа-яіїєґ']+)?$"
    pattern_phone = r"\d{10}"
    def inner(*args, **kwargs):

        try:

            """
            Перевіримо валідність імені користувача в іменованому параметрі
            """

            if func.__name__ == "add_contact" or func.__name__ == "change_contact" or func.__name__ == "show_phone":
                
                if "name" in kwargs:
                
                    if kwargs["name"] is None:
                        raise ValueError("Параметр для іменованого аргументу name не може бути None!")
                    if not kwargs["name"]:
                        raise ValueError("Параметр для іменованого аргументу name не може бути пустим!")
                    if re.fullmatch(pattern_name, kwargs["name"], re.UNICODE) is None:
                        raise ValueError("Значення параметра name має бути валідним іменем латиницею або кирилицею!")
                    
            """
            Перевіримо валідність номера телефону 
            """
            if func.__name__ == "add_contact" or func.__name__ == "change_contact":
                
                if "phone" in kwargs:

                    if kwargs["phone"] is None:
                        raise ValueError("Параметр для іменованого аргументу phone не може бути None!")
                    if not kwargs["phone"]:
                        raise ValueError("Параметр для іменованого аргументу phone не може бути пустим!")
                    if re.fullmatch(pattern_phone, kwargs["phone"], re.UNICODE) is None:
                        raise ValueError("Значення параметра phone має бути валідним номером телефону!")
                
            """
            Перевірка відсутності імені в словнику при зміні номера телефона чи вже присутності імені у словнику при додаванні нового імені у словник
            """

            if func.__name__ == "add_contact" or func.__name__ == "all_users" or func.__name__ == "change_contact" or func.__name__ == "show_phone":
                
                if "users" in kwargs:
                    if kwargs["users"] is None:
                        raise ValueError("Параметр для іменованого аргументу users не може бути None!")
                    if func.__name__ == "add_contact":
                        if kwargs["name"] in kwargs["users"].keys():
                            raise KeyError("Таке ім'я у словнику вже є!")
                    if func.__name__ == "change_contact":
                        if kwargs["name"] not in kwargs["users"].keys():
                            raise KeyError("Такого імені у словнику немає!")
            return func(*args, **kwargs)
                    
        except ValueError as ex:
            return str(ex)
        except KeyError as ex:
            return str(ex)
    return inner

