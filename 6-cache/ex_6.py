

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional


T = TypeVar("T")
R = TypeVar("R")


@dataclass
class Cache(Generic[T, R]):
    _data: dict[T, R] = field(default_factory=dict)

    def set(self, k: T, v: R) -> None:
        self._data[k] = v

    def get(self, k: T) -> Optional[R]:
        return self._data.get(k)

    def keys(self) -> list[T]:
        return list(self._data.keys())

    def values(self) -> list[T]:
        return list(self._data.values())


hits = Cache[str, int]()
hits.set("home", 10)
hits.set("about", 3)
x = hits.get("home")        # x: int | None
paths = hits.keys()         # list[str]
counts = hits.values()      # list[int]

print(f"Key 'home': {x}")
print(f"All keys: {paths}")

hits.set("contacts", "5")   # ❌ ошибка типов
hits.get(123)               # ❌ ошибка типов
