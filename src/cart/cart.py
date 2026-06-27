"""Warenkorb für Aufgabe 2. Entwickelt im TDD"""


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        self.items[name] = quantity

    def item_count(self) -> int:
        return len(self.items)
