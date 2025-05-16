from typing import List, Optional, TYPE_CHECKING
from order import Order

if TYPE_CHECKING:
    from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        self.name = name
        self._orders: List[Order] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be 1 to 15 characters long")
        self._name = value

    def orders(self) -> List[Order]:
        return self._orders.copy()

    def coffees(self) -> List["Coffee"]:
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def create_order(self, coffee: "Coffee", price: float) -> Order:
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee: "Coffee") -> Optional["Customer"]:
        spending = {}
        for order in coffee.orders():
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
        if not spending:
            return None
        max_spent = max(spending.values())
        for customer, amount in spending.items():
            if amount == max_spent:
                return customer
