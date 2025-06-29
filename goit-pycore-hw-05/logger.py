from collections import Counter
import sys

"""
Функція load_logs - завантажує файл з логами, читає порядково
і відправляє рядки у функцію parse_log_line

Аргументи:
file_path: str - рядок зі шляхом до файлу логів

return: list - повертає список словників з даними логів
"""

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                log = parse_log_line(line)
                logs.append(log)
    except FileNotFoundError as ex:
        print("Такого файлу не знайдено " + str(ex))
        return []
    except PermissionError as ex:
        print("Не достатньо прав для відкриття файлу " + str(ex))
        return []
    except IsADirectoryError as ex:
        print("Замість файлу вказано директорію " + str(ex))
        return []
    except UnicodeDecodeError as ex:
        print("Помилка при розпізнаванні кодування " + str(ex))
        return []
    except OSError as ex:
        print("Інша системна помилка " + str(ex))
        return []

    return logs

"""
Функція parse_log_line - з рідка отримує дані логів і повертає
ці дані у вигляді словника

Аргументи:
line: str - рядок з записом одного з логів

return: dict - повертає словник з даними логів
"""

def parse_log_line(line: str) -> dict:
    items = line.split()
    log = {
        "date": items[0],
        "time": items[1],
        "level": items[2],
        "message": " ".join(items[3:])
    }
    return log

"""
Функція filter_logs_by_level - фільтрує логи за рівнем логування

Аргументи: 
logs: list - список словників логів
level: str - рядок рівня логування INFO, DEBUG, ERROR або WARNING

return: list - повертає список словників фільтрованих за рівнем логування
"""

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x["level"].lower() == level.lower(), logs))

"""
Функція count_logs_by_level - підраховує кількість записів кожного з рівнів логування

Аргументи:
logs: list - список словників з даними логів

return: dict - повертає словник з кількостями записів по кожному рівню логування; ключі рівні логування

"""

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs))

"""
Функція display_log_counts - візуалізує кількості записів рівнів логування

Аргументи:
counts: dict - словник з кількостями записів по кожному рівню логування
"""

def display_log_counts(counts: dict):

    print("Рівень логування | Кількість")
    print("-----------------|----------")
    print("INFO             |  " + str(counts["INFO"]))
    print("DEBUG            |  " + str(counts["DEBUG"]))
    print("ERROR            |  " + str(counts["ERROR"]))
    print("WARNING          |  " + str(counts["WARNING"]))

def main():

    """
    Перевіряємо чи всі параметри задані для скрипта.
    Якщо один - недостатньо

    """

    if len(sys.argv) == 1:
        print("Не передані аргументи у скрипт")
        exit(1)

    """
    Якщо задано бодай один параметр код працює далі
    Передаємо рядок зі шляхом до лог-файлу у  load_logs
    Обчислюємо кількість записів логів кожного рівня
    і візуалізуємо результат
    """
    filepath = sys.argv[1]
    logs = load_logs(filepath)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    """
    Якщо маємо ще й параметр level з рівнем логування
    фільтруємо записи за рівнем логування, що передано у якості параметру у скрипт
    """
    if len(sys.argv) > 2:
        level = sys.argv[2]
        logs_level = filter_logs_by_level(logs, level)
        for log in logs_level:
            print(log["message"])

if __name__ == "__main__":
     main()