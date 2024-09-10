import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order():
    pauline = Customer("Pauline")
    latte = Coffee("Latte")
    order = Order(pauline, latte, 5.0)

    assert order.customer == pauline
    assert order.coffee == latte
    assert order.price == 5.0

    with pytest.raises(ValueError):
        Order(pauline, latte, 0)  
