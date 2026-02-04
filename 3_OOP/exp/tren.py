# **Описание**: Реализуйте класс Circle с полем radius, добавьте метод экземпляра get_circumference, который возвращает длину окружности
#
# **Входные данные**: Встроенные данные в коде (радиус окружности)
#
# **Выходные данные**: Длина окружности в виде числа с плавающей точкой
#
# **Ограничения**:
# - Используйте только базовые возможности Python
# - Все данные предоставлены в коде
# - Для вычисления используйте приближенное значение π = 3.14159
# - Не используйте внешние библиотеки
#
# **Примеры**:
# Input: radius=5
# Output: 31.4159
#
# Input: radius=10
# Output: 62.8318

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_circumference(self):
        dl = 2 * 3.14159 * self.radius
        return float(dl)


dld1 = Circle(5)
dld2 = Circle(10)
print(dld1.get_circumference())
print(dld2.get_circumference())
