"""Warenkorb für Aufgabe 2. Entwickelt im TDD"""

class CartError(Exception):
    """Basisklasse für fachliche Fehler im Warenkorb"""
    pass


class ItemNotFoundError(CartError):
    """Fehlerklasse für zu entfernenden Artikel, der aber nicht im Warenkorb ist"""
    pass


class CartItem:
    """Stellt ein Artikelobjekt des Warenkorbs dar"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_total(self) -> float:
        return self.price * self.quantity


class ShoppingCart:
    """Stellt den Warenkorb dar und stellt entsprechende Funktionen zur Verfügung"""
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Fügt einen Artikel in einer bestimmten Menge zum Warenkorb zu"""
        if quantity <= 0 or price <= 0:
            raise CartError("Mengenangabe ungültig")
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = CartItem(name, price, quantity)

    def item_count(self) -> int:
        """Gibt die Gesamtzahl aller Artikel aus"""
        total = 0
        for item in self.items.values():
            total += item.quantity
        return total

    def total(self):
        total = 0
        for item in self.items.values():
            total += item.line_total()
        return total

    def remove_item(self, name: str) -> None:
        """Entfernt einen Artikel vom Warenkorb"""
        if name not in self.items:
            raise ItemNotFoundError(f"Artikel {name} ist nicht im Warenkorb")
        del self.items[name]

    def apply_discount(self, percent: float) -> float:
        """Berechnet anhand eines Rabatts den Gesamtpreis für den Warenkorb"""
        if percent <= 0 or percent > 100:
            raise CartError("Rabatt muss zwischen 0 und 100 liegen")
        return self.total() * (1 - percent / 100)