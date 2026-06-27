import pytest
from cart.cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item('apple', 0.50)
    assert cart.item_count() == 1

def test_add_item_increases_quantity(cart):
    cart.add_item('apple', 0.50, 2)
    cart.add_item('apple', 0.50, 3)
    assert cart.item_count() == 5

def test_add_item_zero_quantity_raises(cart):
    with pytest.raises(CartError):
        cart.add_item('apple', 0.50, 0)

def test_add_item_negative_quantity_raises(cart):
    with pytest.raises(CartError):
        cart.add_item('apple', 0.5, -5)


