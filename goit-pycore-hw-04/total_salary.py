"""
Функція total_salary розраховує загальну та середню
заробітні плати усіх розробників компанії

Аргументи:
path: str - приямає рядок шлях до файлу з переліком співробітників та їх заробітними платами

return: tuple - повертає кортеж з двох чисел (загальна, середня) заробітні плати
"""

def total_salary(path: str) -> tuple:

    """
    Прочитаємо усі дані з файлу path у список entries
    Визначимо загальну заробітну плату, отримавши список числових
    значень заробітних плат та привівши їх до цілочисельного значення
    Також, визначимо середню заробітну плату, розділивши
    загальну заробітну плату на кількість розробників
    """
    try:

        with open(path, encoding="utf-8") as f:
            entries = f.readlines()
            common_salary = sum([int(val.split(',')[1]) for val in entries])
            average_salary = common_salary / len(entries)

    except FileNotFoundError as ex:
        """
        Якщо файл відсутній, кидаємо виключення FileNotFoundError
        """

        print(str(ex) + " Файл відсутній")
        return ()
    except ZeroDivisionError as ex:
        """
        Якщо у файлі з розробниками немає списку імен, відбудеться ділення на нуль
        записів. Відповідно обробляємо дану ситуацію.
        """

        print(str(ex) + " Ділення на нуль неможливе!")
        return ()
    except BaseException as ex:
        """
        Обробляємо інші варіанти помилок
        """
        print(str(ex))
        return ()
    
    """
    Повернімо кортеж із загальної та середньої заробітних плат
    """
    
    return (common_salary, average_salary)

print(total_salary(""))
        
        
