import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def test_name_property(self):
        coffee = Coffee("Mocha")
        self.assertEqual(coffee.name, "Mocha")
        with self.assertRaises(AttributeError):
            coffee.name = "Espresso"
        with self.assertRaises(ValueError):
            Coffee("ab")

    def test_orders_and_customers(self):
        coffee = Coffee("Cappuccino")
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        order1 = c1.create_order(coffee, 4.0)
        order2 = c2.create_order(coffee, 6.0)
        self.assertIn(order1, coffee.orders())
        self.assertIn(order2, coffee.orders())
        self.assertIn(c1, coffee.customers())
        self.assertIn(c2, coffee.customers())

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Americano")
        c = Customer("Charlie")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0.0)
        c.create_order(coffee, 5.0)
        c.create_order(coffee, 7.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()
