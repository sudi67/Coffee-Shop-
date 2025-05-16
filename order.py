from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee

class Order:
    def __init__(self, customer: "Customer", coffee: "Coffee", price: float):
        if not isinstance(customer, object) or customer.__class__.__name__ != "Customer":
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, object) or coffee.__class__.__name__ != "Coffee":
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self) -> "Customer":
        return self._customer

    @property
    def coffee(self) -> "Coffee":
        return self._coffee

    @property
    def price(self) -> float:
        return self._price
