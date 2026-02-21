

from dataclasses import dataclass
from typing import Generic, TypeVar


@dataclass
class IntBox:
    value: int

    def get(self):
        return self.value


T = TypeVar("T")


@dataclass
class Box(Generic[T]):
    value: T

    def get(self) -> T:
        return self.value


int_box = Box(1)
int_box.get()
