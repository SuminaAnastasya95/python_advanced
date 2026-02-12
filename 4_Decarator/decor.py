"""Позволяет обернуть одну функцию в другую и модифицировать ее поведение"""


def log_decorator(func):
    def wrapper():
        print("Функция началась")
        func()
        print("Функция завершилась")
    return wrapper


@log_decorator  # функция, которая принимает другую функцию
def say_hello():
    print("Hello!")


say_hello()
