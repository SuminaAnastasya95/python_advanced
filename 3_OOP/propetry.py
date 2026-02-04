"""property"""


class Rectangle:
    def __init__(self, width: float, hieght: float) -> None:
        self.width = width
        self.hieght = hieght

    @property
    def area(self):
        """Площадь. При добавления декаратора проперти у нас становится это свойством"""
        return self.hieght * self.width


rect = Rectangle(10, 5)
print(rect.area)
