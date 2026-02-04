"""Игра Герой"""


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, amount: int):
        """получение урона"""
        if not self.is_alive:
            print(f"{self.name} уже погиб")
            return
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} теперь погиб")
        else:
            print(f"Получил {self.name} получил {amount} урона")

    def heal(self, amount):
        """лечение"""
        if not self.is_alive:
            print(f"{self.name} уже погиб")
            return
        self.hp = min(self.hp + amount, 100)
        print(f"{self.name} восстановил {amount} HP. Текущее HP - {self.hp}")

    def add_item(self, item: str):
        """добавление предмета"""
        self.inventory.append(item)
        print(
            f"{self.name} добавил {item} в свой инвентарь. Текущий инвентарь - {self.inventory}")

    def show_status(self):
        """Показ статуса"""
        status = "Жив" if self.is_alive else "Повержен"
        print(
            f"{self.name} HP - {self.hp}, инвентарь - {self.inventory}, Статус - {status}")


hero = Hero("Вася")
hero.add_item("Меч")
hero.show_status()
hero.take_damage(10)
hero.show_status()
hero.heal(10)
hero.show_status()
