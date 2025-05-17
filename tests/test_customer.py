import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_setter_getter(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")
        with self.assertRaises(ValueError):
            c.name = ""
        with self.assertRaises(TypeError):
            c.name = 123

    def test_create_order_and_orders(self):
        c = Customer("Bob")
        coffee = Coffee("Latte")
        order = c.create_order(coffee, 5.0)
        self.assertIn(order, c.orders())
        self.assertIn(coffee, c.coffees())

    def test_most_aficionado(self):
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        coffee = Coffee("Espresso")
        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 7.0)
        self.assertEqual(Customer.most_aficionado(coffee), c2)

if __name__ == "__main__":
    unittest.main()
