import sys

# 1. Обычный класс


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 2. Класс с использованием __slots__


class SlotUser:
    __slots__ = ['name', 'email', 'password']

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


def get_size(objects):
    # Суммируем размер самих объектов в списке
    return sum(sys.getsizeof(obj) for obj in objects)


# Создаем по 100 000 экземпляров
count = 100_000

# Для чистоты эксперимента используем одинаковые строки
name, email, pwd = "Ivan", "ivan@example.com", "secret123"

users = [User(name, email, pwd) for _ in range(count)]
slots_users = [SlotUser(name, email, pwd) for _ in range(count)]

# Расчет памяти
size_regular = get_size(users) / 1024 / 1024  # в Мегабайтах
size_slots = get_size(slots_users) / 1024 / 1024

print(f"Количество объектов: {count:,}")
print("-" * 30)
print(f"Обычный класс (User):     {size_regular:.2f} MB")
print(f"Класс со __slots__ (SlotUser): {size_slots:.2f} MB")
print("-" * 30)
print(f"Экономия: {((size_regular - size_slots) / size_regular) * 100:.1f}%")
