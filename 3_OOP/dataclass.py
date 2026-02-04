"""Декаратор дата класс. Готовый класс, с которым можно сразу работать без дополнительных штук"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    secter_key: str = field(repr=False, compare=False)
    priority: int = 3
    done: bool = False
    create_at: datetime | None = None

    def __post_init__(self):
        if self.create_at is None:
            self.create_at = datetime.now()


task1 = Task("Сделать лекцию", "my_secret")
task2 = Task("Сделать лекцию", "my_secret")
print(task1)
print(task1 == task2)
