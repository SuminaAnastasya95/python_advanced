class User:
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.__balance = balance  # Чтобы параметр сделать приватным необходимо сделать это "__" перед атрибутом. Использовать его внутри класса возможно, но использовать за пределами уже не возможно

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма должна быть положительной")

    def withdraw(self, amount: float):
        if 0 < amount < self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств")


u = User("Настя", 1000)
u.deposit(500)
print(u.get_balance())
u.withdraw(1000)
print(u.get_balance())
print(u.__dict__)
# {'name': 'Настя', '_User__balance': 500} таким образом мы не даем напрямую взаимодействовать с нашим балансом

u.__balance = 500
# {'name': 'Настя', '_User__balance': 500, '__balance': 500}
# Добавилось новое свойство, но наше приватное свойство не поменялось
print(u.__dict__)


u._User__balance = 100
print(u.__dict__)
# {'name': 'Настя', '_User__balance': 100, '__balance': 500}
# Изменение произойдет, но так делать не хорошо, потому что мы обращаемся на прямую
