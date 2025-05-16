# Coffee Shop Domain Model

This project models a coffee shop domain with three main entities: Coffee, Customer, and Order.

## Entities

### Coffee
- **id**: Primary key
- **name**: Name of the coffee
- **price**: Price of the coffee

### Customer
- **id**: Primary key
- **name**: Name of the customer
- **email**: Email of the customer

### Order
- **id**: Primary key
- **coffee_id**: Foreign key referencing Coffee
- **customer_id**: Foreign key referencing Customer

## Relationships

- **Coffee has many Orders**: A single type of coffee can be ordered multiple times by different customers.
- **Customer has many Orders**: A single customer can place multiple orders.
- **Order belongs to a Customer and to a Coffee**: Each order is associated with one customer and one type of coffee.
- **Coffee - Customer is a many-to-many relationship**: This is facilitated through the Order model, which acts as a junction table.

## Setup

1. Install SQLAlchemy:
   ```bash
   pip install sqlalchemy
