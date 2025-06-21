
"""
Функція get_cats_info обробляє файл з інформацією про кішок
та повертає список словників з інформасацією про кожну кішку

Аргументи:
path: str - рядок шлях до файлу з інформацією про кішок

return: list - повертає список словників з інформацією про кожну кішку або пустий список
"""


def get_cats_info(path: str) -> list:

    """
    Прочитаємо файл path і отримаємо список словників інформації 
    про кожну кішку. 
    """

    try:

        with open(path, encoding="utf-8") as f:
            entries = f.readlines()
            list_cats = [
                {
                    "id": val.split(',')[0],
                    "name": val.split(',')[1],
                    "age": int(val.split(',')[2])
                }
                for val in entries
                ]

    except FileNotFoundError as ex:
        """
        Якщо файл не знайдено кидаэмо виключення
        """
        print(str(ex) + " Файл не знайдено!")
        return []
    
    except BaseException as ex:
        """
        Обробляємо інші варіанти виключень
        """
        print(str(ex))
        return []
    
    return list_cats

print(get_cats_info("goit-pycore-hw-04\info_cats.txt"))