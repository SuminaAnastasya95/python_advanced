class Order:
    def __init__(self, number: int, total: float):
        self.number = number
        self.total = total
        print(f"Создан заказ #{number} на сумму {total}")

    def process(self):
        print("Заказ создан")


class EmailOrder(Order):
    def __init__(self, number: int, total: float, email: str):
        super().__init__(number, total)
        self.email = email

    def process(self):
        super().process()
        print("Письмо отправлено")


e = EmailOrder(10, 1, "dd@d.ru")
e.process()
