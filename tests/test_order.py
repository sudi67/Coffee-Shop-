import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_properties(self):
        c = Customer("Dave")
        coffee = Coffee("Flat White")
        order = Order(c, coffee, 4.5)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)

    def test_order_price_validation(self):
        c = Customer("Eve")
        coffee = Coffee("Macchiato")
        with self.assertRaises(TypeError):
            Order(c, coffee, "5.0")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(c, coffee, 11.0)

    def test_order_customer_coffee_validation(self):
        coffee = Coffee("Mocha")
        with self.assertRaises(TypeError):
            Order("not a customer", coffee, 5.0)
        c = Customer("Frank")
        with self.assertRaises(TypeError):
            Order(c, "not a coffee", 5.0)

if __name__ == "__main__":
    unittest.main()
