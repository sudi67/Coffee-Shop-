from typing import List, TYPE_CHECKING
from order import Order

if TYPE_CHECKING:
    from customer import Customer

class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name
        self._orders: List[Order] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Coffee name is immutable once set")

    def _add_order(self, order: Order):
        self._orders.append(order)

    def orders(self) -> List[Order]:
        return self._orders.copy()

    def customers(self) -> List["Customer"]:
        unique_customers = []
        for order in self._orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers

    def num_orders(self) -> int:
        return len(self._orders)

    def average_price(self) -> float:
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
