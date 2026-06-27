"""Warenkorb für Aufgabe 2. Entwickelt im TDD"""

class CartItem:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = CartItem(name, price, quantity)

    def item_count(self) -> int:
        total = 0
        for item in self.items.values():
            total += item.quantity
        return total
