# Типы событий
# ClickEvent:
# Параметры: координаты x и y (оба типа int).
# KeyEvent:
# Параметр: кнопка key (типа str).
# ResizeEvent:
# Параметры: width и height (оба типа int).

from dataclasses import dataclass


@dataclass
class ClickEvent:
    x: int
    y: int


@dataclass
class KeyEvent:
    key: str


@dataclass
class ResizeEvent:
    width: int
    height: int


def handle_event(ev: ClickEvent | KeyEvent | ResizeEvent) -> str:
    match ev:
        case ClickEvent(x=x, y=y):
            return f'Click at {x}, {y}'
        case KeyEvent(key=k):
            return f'Pressed  {k}'
        case ResizeEvent(width=w, height=h):
            return f'Resized {w} x {h}'
    raise ValueError("Неизвестное событие")


print(handle_event(ClickEvent(1, 10)))
print(handle_event(KeyEvent("ssss")))
print(handle_event(ResizeEvent(1920, 1080)))
