import pytest
from cart.cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    cart.add_item('apple', 0.50)
    assert cart.item_count() == 1


