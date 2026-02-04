"""Имеет доступ к классу, но не имеет доступ к экземпляру"""


class User:
    """Пользователь"""
    users = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        User.users.append(self)

    @classmethod
    def from_string(cls, data: str):
        """Альтернативное создание"""
        name, age = data.split(",")
        return cls(name, int(age))

    @classmethod
    def total_users(cls):
        """Число пользователей"""
        return len(cls.users)


vasia = User("Вася", 15)
kate = User("Катя", 25)
print(vasia.total_users())
print(User.total_users())


maxim = User.from_string("Макс, 40")
print(maxim.name, maxim.age)
