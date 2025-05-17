from customer import Customer
from coffee import Coffee

def main():
    print("Welcome to the Coffee Shop CLI Demo!")
    # Create some customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create some coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Create orders
    alice.create_order(latte, 4.5)
    alice.create_order(espresso, 3.0)
    bob.create_order(latte, 5.0)

    # Show orders for Alice
    print(f"Orders for {alice.name}:")
    for order in alice.orders():
        print(f"  Coffee: {order.coffee.name}, Price: ${order.price}")

    # Show coffees Bob has ordered
    print(f"Coffees ordered by {bob.name}: {[coffee.name for coffee in bob.coffees()]}")

    # Show number of orders for Latte
    print(f"Number of orders for {latte.name}: {latte.num_orders()}")

    # Show average price for Latte
    print(f"Average price for {latte.name}: ${latte.average_price():.2f}")

    # Show most aficionado for Latte
    aficionado = Customer.most_aficionado(latte)
    if aficionado:
        print(f"Most aficionado for {latte.name}: {aficionado.name}")
    else:
        print(f"No orders for {latte.name} yet.")

if __name__ == "__main__":
    main()
