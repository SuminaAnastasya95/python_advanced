"""Если функции имеют аргументы"""


def log(func):
    """Функция логирования"""
    def wrapper(*args, **kwargs):
        print(
            f'Вызов нашей функции {func.__name__} с аргументами {args}{kwargs}')
        result = func(*args, **kwargs)
        print("готово")
        return result
    return wrapper


@log
def add(a: float, b: float):
    return a + b


print(add(2, 5))
