# softwaretechnik-testing
Dient zur Erledigung von Aufgaben im Modul Softwaretechnik und zur Abgabe der Einsendeaufgabe

## Aufgabe 1

Aufgabe ist in den Files calculator.py und test_calculator.py bearbeitet.


## Aufgabe 2 

Aufgabe ist in den Dateien cart.py, test_cart.py und den damit verbundenen git commits bearbeitet und erfüllt

## Aufgabe 4

Mutation Testing mit mutmut:

### ZUSAMMENFASSUNG

```
⠇ Generating mutants
    done in 746ms (4 files mutated, 0 ignored, 0 unmodified)
⠏ Running stats
    done
⠹ Running clean tests
    done
⠇ Running forced fail test
    done
Running mutation testing
⠴ 66/66  🎉 41 🫥 0  ⏰ 0  🤔 0  🙁 25  🔇 0  🧙 0
34.30 mutations/second
```

### RESULTS

```
    calculator.calculator.xǁCalculatorǁdivide__mutmut_3: survived
    calculator.calculator.xǁCalculatorǁdivide__mutmut_4: survived
    calculator.calculator.xǁCalculatorǁdivide__mutmut_5: survived
    calculator.calculator.xǁCalculatorǁdivide__mutmut_6: survived
    cart.cart.xǁCartItemǁ__init____mutmut_1: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_2: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_4: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_5: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_6: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_7: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_10: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_11: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_12: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_13: survived
    cart.cart.xǁShoppingCartǁadd_item__mutmut_18: survived
    cart.cart.xǁShoppingCartǁremove_item__mutmut_2: survived
    cart.cart.xǁShoppingCartǁitem_count__mutmut_3: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_2: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_3: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_4: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_5: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_6: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_7: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_8: survived
    cart.cart.xǁShoppingCartǁapply_discount__mutmut_9: survived
```

### Analyse Beispiel 1

Nehme cart.cart.xǁShoppingCartǁremove_item__mutmut_2:

```
#cart.cart.xǁShoppingCartǁremove_item__mutmut_2: survived
--- src/cart/cart.py
+++ src/cart/cart.py
@@ -1,4 +1,4 @@
 def remove_item(self, name: str) -> None:
     if name not in self.items:
-        raise ItemNotFoundError(f"Artikel '{name}' ist nicht im Warenkorb.")
+        raise ItemNotFoundError(None)
     del self.items[name]
```

Hier zeigt sich, dass der Testfall überlebt hat, weil lediglich nach der geworfenen ItemNotFoundError-Exception geprüft
wird. Es wird nicht geprüft, welchen Inhalt diese hat. Für eine saubere Nachverfolgung der Exception, sollte der
Testfall ebenfalls auf den message text prüfen.


### Analyse Beispiel 2

Nehme cart.cart.xǁShoppingCartǁapply_discount__mutmut_2:


```
# cart.cart.xǁShoppingCartǁapply_discount__mutmut_2: survived
--- src/cart/cart.py
+++ src/cart/cart.py
@@ -1,4 +1,4 @@
 def apply_discount(self, percent: float) -> float:
-    if percent < 0 or percent > 100:
+    if percent <= 0 or percent > 100:
```

Hier weist der mutierte Testfall auf eine fachliche Fragestellung, die es festzulegen gilt: Ist ein Rabatt von 0 % eine
sinnvolle Berechnungsgrundlage? Vermutlich nicht, also könnte der mutierte Testfall ("percent <= 0") den eigentlichen
Testfall ("percent < 0") in diesem Fall sogar ersetzen.