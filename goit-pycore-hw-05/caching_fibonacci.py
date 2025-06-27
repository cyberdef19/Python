
"""
Функція для обчислення чисел Фібоначчі
створює та використовує кеш для зберігання та повторного
використання значень чисел Фібоначчі.

"""

def caching_fibonacci():
    """
    Створення словника кешу пустого
    """
    cache = {}
    def fibonacci(n):

        """
        Якщо n - від'ємне або 0, то повертаємо 0
        Якщо n - дорівнює 1, то повертаємо 1
        Якщо n міститься в cache то повертаємо значення по ключу,
        щоб не обчислювати його повторно
        Якщо такого значення немає в словнику, обчислюємо

        Повертаємо значення по обчисленому ключу
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]
    return fibonacci

fibonacci = caching_fibonacci()
print(fibonacci(10))
print(fibonacci(15))
