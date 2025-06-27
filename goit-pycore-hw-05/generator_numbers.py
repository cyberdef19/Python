import re 
from decimal import Decimal
from typing import Callable

"""
Функція generator_numbers - генератор що генерує дійсні числа
визначаючи їх у переданому аргументом тексті.

Аргументи: 
text: str - текст, в якому є дійсні числа
повертає об'єкт генератора
"""

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):

    """
    Визначимо паттерн, який буде шукати дійсні числа в тексті
    Знайдемо усі значення дійсних чисел.
    """
    pattern = r"\d+\.*\d+"
    matches = re.findall(pattern=pattern, string=text)

    """
    Кожне знайдене значення дійсного числа приведемо до
    типу Decimal з метою не допускати помилок обчислення
    та повернемо це значення за допомогою yield
    """
    for item in matches:
        val = Decimal(item.strip())
        yield val

"""
Функція sum_profit обчислює сумму усіх знайдених дійсних чисел

АргументиЖ
text: str - рядок тексту, в якому знаходяться також дійсні числа
func: Callable - функція, що має бути викликана у sum_profit
і в яку у якості параметра буде передано text

return  - повертає дійсне число
"""

def sum_profit(text:str, func: Callable) -> Decimal:
    sum = Decimal("0.0")
    for val in func(text):
        sum = sum + val
    return sum

print(sum_profit(text, generator_numbers))
    
