
from dataclasses import dataclass
from typing import Protocol


class DiscountPolicy(Protocol):
    def discount(self, total: float) -> float: ...


class NoDiscount:
    def discount(self, total: float) -> float:
        return 0


@dataclass
class PersentDiscount:
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100)


@dataclass
class Item:
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        return self.price * self.qty

    # : Если метод discount отсутствует в классе, это может привести к ошибкам, которые не будут видны в IDE до момента выполнения.


@dataclass
class Order:
    items: list[Item]
    policy: DiscountPolicy

    def total(self):
        return sum(i.subtotal() for i in self.items)

    def total_w_discount(self):
        t = self.total()
        return t - self.policy.discount(t)

    def set_policy(self, policy: DiscountPolicy):
        self.policy = policy


basket = [Item("Бумага", 100, 5), Item("Яблоки", 10, 15)]
order = Order(basket, NoDiscount())
print(order. total())
print(order. total_w_discount())
order.set_policy(PersentDiscount(10))
print(order. total())
print(order. total_w_discount())
