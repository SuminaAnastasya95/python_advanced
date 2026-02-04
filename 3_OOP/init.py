"""Зарезервированный метод, он вызывается автоматически , когда создается новый экземпляр класса"""


class Note:
    """Заметка"""
    # title: str
    # description: str
    # атрибуты мы можен опустить, потому что их можно объявить в init
    default_description = "Описания нет"

    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description or self.default_description


note = Note("Заметка", "Это моя заметка")
print(note.description)
note_next = Note("моя заметка")
