"""Встроенные методы"""


class ShoppingList:
    """Список покупок"""

    def __init__(self, items: list[str]):
        self.items: list[str] = items

    def __eq__(self, value: object) -> bool:
        """Втроеный метод равенства именно самих данных"""
        if not isinstance(value, ShoppingList):
            return False
        return self.items == value.items

    def __len__(self):
        """Втсроенная функция опредляет длину объекта"""
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self) -> str:
        return f"Shopping_List(items = {",".join(self.items)})"


list_1 = ShoppingList(["Apple"])
list_2 = ShoppingList(["Potate"])


print(len(list_1))
print(list_1[0])
print(list_1 == list_2)
print(list_1)
