"""
Функція parse_input обробляє користувацький ввод custom_input
отримує команду та список аргументів і переводить 
команду до нижнього регістру

Аргументи:
custom_input: str - користувацький ввод [команда] [список аргументів] через пробіл

return: tuple - повертає кортеж з команди та списку аргументів
"""


def parse_input(custom_input: str) -> tuple:
    cmd, *args = custom_input.split()
    cmd = cmd.strip().lower()
    return (cmd, *args)
