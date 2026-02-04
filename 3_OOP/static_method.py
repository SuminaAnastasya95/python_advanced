"""Стаические методы не имеют доступа к классу/ объекту мы ее просто поместили туда, но она имеет возможность выполнять какие-то дейстия"""
# Зачем это нужно?
# Нам нужно чтобы этот метод выполнялся, но не зависел от нашего класса/ объекта. А мы их объединяем в один класс для удобства дальнейшего использования
from datetime import date


class Book:
    """Книга"""

    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    @staticmethod
    def year_since(year: int) -> int:
        """Сколько лет книге"""
        return date.today().year - year


book = Book("Властелин колец", 1985)
print(Book.year_since(book.year))
