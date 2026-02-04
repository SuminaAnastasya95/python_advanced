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

    def transfer_to(self, other_account: 'BankAccount', amount: float):
        """Фактический перевод денег на другой счет BankAccount"""
        # 1. Проверка: является ли получатель объектом BankAccount
        if not isinstance(other_account, BankAccount):
            return "Ошибка: Получатель должен быть зарегистрированным аккаунтом"

        # 2. Проверка: не пытаемся ли перевести сами себе
        if self.account == other_account.account:
            return "Невозможно перевести средства на тот же аккаунт"

        # 3. Проверка суммы
        if amount <= 0:
            return "Сумма перевода должна быть положительной"

        # 4. Логика перевода:
        if self.balance >= amount:
            self.balance -= amount          # Списываем у себя
            other_account.balance += amount  # Зачисляем другому
            return (f"Перевод выполнен успешно!\n"
                    f"Списано с {self.account}: {amount:.2f}\n"
                    f"Зачислено на {other_account.account}: {amount:.2f}\n"
                    f"Ваш текущий баланс: {self.balance:.2f}")
        else:
            return f"Недостаточно средств для перевода. Текущий баланс: {self.balance:.2f}"

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
