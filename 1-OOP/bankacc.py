"""Мини банковское приложение"""


class BankAccount:
    accounts = []

    def __init__(self, name: str, account: str | int, balance: float = 0):
        self.name = name
        self.account = account
        self.balance = balance

        BankAccount.accounts.append(self)

    def deposit(self, amount: float):
        """пополнение счёта на сумму amount"""
        if amount < 0:
            return f"Сумма пополнения должна быть положительной: <{amount}>"
        else:
            self.balance += amount
            return f"Баланс после пополнения - {float(self.balance):.2f}"

    def withdraw(self, amount: float):
        """снятие денег со счёта. Нельзя уйти в минус"""
        if amount > self.balance:
            return f"Сумма снятия: <{amount}> превышает баланс аккаунат: <{self.balance}>"
        elif amount <= 0:
            return f"Сумма снятия должна быть положительной: <{amount}>"
        else:
            self.balance -= amount
            return f"Баланс после снятия - {float(self.balance):.2f}"

    def transfer_to(self, otheraccount: str | int, amount: float):
        if amount > self.balance:
            return f"Сумма снятия: <{amount}> превышает баланс аккаунат: <{self.balance}>"
        elif amount < 0:
            return f"Сумма снятия не может быть отрицательной: <{amount}>"
        elif self.balance > 0:
            return f"Недостаточно средств для осуществления перевода. Текущий баланс: <{self.balance}>"
        elif int(self.account) == int(otheraccount) or str(self.account) == str(otheraccount) or str(self.account) == int(otheraccount) or int(self.account) == str(otheraccount):
            return "Невозможно перевести средстна на один и тот же аккаунт"
        else:
            result_withdraw = self.balance - amount
            self.balance = result_withdraw
            return f"Осуществлен перевод с аккаунта: {self.account}, на аккаунт: {otheraccount}, на сумму: <{amount}>. Итоговый баланс: {float(self.balance):.2f}"

    def info(self):
        return f"\nПользователь счета: {self.name}\nНомер счета: {self.account}\nИтоговый баланс: {self.balance}"

    @classmethod
    def getaccountscreated(cls):
        """возвращает количество созданных счетов"""
        return len(cls.accounts)


acc1 = BankAccount("Boba", "101", 1000)
acc2 = BankAccount("Bibis", "102", 500)

print(acc1.deposit(500))         # Пополнение
print(acc1.transfer_to('otheraccount', 300))  # Перевод от Boba к Bibis
print(acc1.info())               # Баланс 1200
print(acc2.info())
print(BankAccount.getaccountscreated())
