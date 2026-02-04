"""Описание марки машин"""


class Car:
    mark: str
    model: str
    years: int
    # Значение по умолчанию, если не задано значение. Когда появляется значение в экземплере, тогда
    vahicle_type: str = "Легковой"


audi = Car()
audi.mark = "Audi"
print(audi.vahicle_type)
audi.vahicle_type = 'Лодки'
print(audi.vahicle_type)

Car.vahicle_type = 'Грузовой'
print(audi.vahicle_type)


# Типизация лодки все равно сохраниться, но ее лучше не игнорировать!
class Boat:
    """Лодки"""
    pass


boat1 = Boat()
boat1.years = 2025
print(boat1.years)
