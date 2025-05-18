# Coffee Shop Domain Model

This project models a coffee shop domain with three main entities: Coffee, Customer, and Order.

## Entities

### Coffee
- **name**: Name of the coffee (string, at least 3 characters)
- Has many Orders
- Has many Customers through Orders

### Customer
- **name**: Name of the customer (string, 1–15 characters)
- Has many Orders
- Has many Coffees through Orders

### Order
- Belongs to a Customer and a Coffee
- Has a price (float, 1.0–10.0)

## Relationships

- Coffee has many Orders: A single type of coffee can be ordered multiple times by different customers.
- Customer has many Orders: A single customer can place multiple orders.
- Order belongs to a Customer and to a Coffee: Each order is associated with one customer and one type of coffee.
- Coffee - Customer is a many-to-many relationship facilitated through the Order model.

## Setup

1. Create and activate a Python virtual environment (recommended):
   ```bash
   pipenv install
   pipenv shell
   ```

2. Run the debug demo script:
   ```bash
   python debug.py
   ```

3. Run the unit tests:
   To avoid import errors, run tests with the PYTHONPATH environment variable set to the current directory:
   ```bash
   # Run all tests
   PYTHONPATH=. pytest

   # Run a specific test file
   PYTHONPATH=. pytest tests/test_customer.py

   # Run tests with detailed output
   PYTHONPATH=. pytest -v

   # Run tests and stop after first failure
   PYTHONPATH=. pytest -x
   ```
   python debug.py

## Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py
```

