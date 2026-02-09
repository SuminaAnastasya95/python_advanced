
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        return self.price * self.qty


class NoDiscount:
    def discount(self, total: float) -> float:
        return 0


@dataclass
class PersentDiscount:
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100)


class Order:
    def __init__(self, items: list[Item], police):
        self.items = items
        self.policy = police

    def total(self):
        return sum(i.subtotal() for i in self.items)

    def total_w_discount(self):
        t = self.total()
        return t - self.policy.discount(t)

    def set_policy(self, policy):
        self.policy = policy


basket = [Item("Бумага", 100, 5), Item("Яблоки", 10, 15)]
order = Order(basket, NoDiscount())
print(order. total())
print(order. total_w_discount())
order.set_policy(PersentDiscount(10))
print(order. total())
print(order. total_w_discount())
