
class Payment():
    def pay(self, amount: int):
        raise NotImplementedError("метод должен быть определен")


# По-хорошему используется наследование, но здесь он больше для проверки, потому что мы можем допустить ошибку в названии метода и тогда мы упадем, а в данном случае, когда мы сделали класс, который наследуется, и если мы ошиблись, тогда упадет изместная нам ошибка


class CardPay(Payment):
    def pay(self, amount: float):
        return f"Оплата картой - {amount}"


class CriptoPay(Payment):
    def pay(self, amount: float):
        return f"Оплата криптой - {amount}"


class ApplePay(Payment):
    def psay(self, amount: float):
        return f"Оплата apple - {amount}"


payment = [CardPay(), CriptoPay(), ApplePay()]

for p in payment:
    print(p.pay(100))
