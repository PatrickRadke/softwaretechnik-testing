"""Kleiner Taschenrechner für die Aufgabenstellung A1 (Unit-Tests mit mindestens einem Exception Test)"""

class DivisionByZeroError(ValueError):
    """Wird geworfen, wenn durch Null geteilt werden soll"""


class Calculator:
    """Grundrechenarten mit minimaler Eingabeprüfung."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Division durch Null ist nicht erlaubt.")
        return a / b

    def is_even(self, n: int) -> bool:
        return n % 2 == 0