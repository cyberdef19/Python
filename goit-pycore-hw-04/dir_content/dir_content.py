from pathlib import Path
from colorama import Fore, Style, init
import sys

init(autoreset=True)
"""
Функція dir_content обробляє вказаний користувачем шлях до директорії,
візуалізуючи структуру даної директорії, виводячи піддиректорії та файли

Аргументи:
path: pathlib.Path - приймає рядок шлях до директорії у вигляді об'єкту типу Path

return: - функція нічого не повертає
"""

def dir_content(path: Path, level: int = 0):
    """
    Створимо відступи для кожного виводу вкладених об'єктів
    """
    prefix = "    " * level
    for item in path.iterdir():
        """
        Пройдемося по об'єктам директорії, якщо файл - просто виводимо на консоль
        якщо директорія - зайдемо також у цю директорію та перелічимо все що там є
        """
        if item.is_dir():
            print(prefix + Fore.BLUE + str(item.name) + "\\" + Style.RESET_ALL)
            dir_content(item, level + 1)       
        elif item.is_file():
            print(prefix + Fore.RED + str(item.name) + Style.RESET_ALL)

if __name__ == "__main__":

    """
    Отримаємо аргумент командного рядка для визначення
    структури папок та файлів у передайній директорії. Якщо 
    аргументів у sys.argv всього один, визначаємо, що не вказано
    шлях до необхідної директорії. Якщо ж аргументів більше ніж 2
    обробляємо лише один
    """

    """
    Перевіримо наявність достатньої кількості аргументів
    """
    
    if len(sys.argv) > 1:
       
        arg = sys.argv[1]
        path = Path(arg)

        """
        Перевіримо чи переданий аргумент є директорією та чи ця директорія є абсолютним шляхом
        """
        if path.is_dir():
            if path.is_absolute():
                """
                Виконаємо функцію перелічення об'єктів цільової директорії
                """
                dir_content(path)
            else:
                print("Переданий шлях відносний. Потрібен абсолютний шлях до директорії.")
        else:
            print("Вказаний шлях - шлях до файлу, а не до директорії")
        

    else:
        print("Не вказано шлях до директорії")