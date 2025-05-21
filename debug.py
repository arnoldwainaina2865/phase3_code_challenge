from customer import Customer
from coffee import Coffee
from order import Order


try:
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    print(f"Created customers: {alice.name}, {bob.name}, {charlie.name}")
except Exception as e:
    print(f"Error creating customers: {e}")


try:
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    print(f"Created coffees: {espresso.name}, {latte.name}, {cappuccino.name}")
except Exception as e:
    print(f"Error creating coffees: {e}")

try:
    
    alice_order1 = alice.create_order(espresso, 3.5)
    alice_order2 = alice.create_order(latte, 4.5)
    alice_order3 = alice.create_order(espresso, 3.5)
    
    
    bob_order1 = bob.create_order(latte, 4.0)
    bob_order2 = bob.create_order(cappuccino, 5.0)
    
    
    charlie_order1 = charlie.create_order(espresso, 3.0)
    charlie_order2 = charlie.create_order(cappuccino, 5.5)
    
    print("Created orders successfully")
except Exception as e:
    print(f"Error creating orders: {e}")


print("\n--- Customer Methods ---")
try:
    print(f"Alice's orders count: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    
    print(f"Bob's orders count: {len(bob.orders())}")
    print(f"Bob's coffees: {[coffee.name for coffee in bob.coffees()]}")
except Exception as e:
    print(f"Error testing customer methods: {e}")


print("\n--- Coffee Methods ---")
try:
    print(f"Espresso orders count: {espresso.num_orders()}")
    print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
    print(f"Espresso average price: ${espresso.average_price():.2f}")
    
    print(f"Latte orders count: {latte.num_orders()}")
    print(f"Latte customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte average price: ${latte.average_price():.2f}")
except Exception as e:
    print(f"Error testing coffee methods: {e}")


print("\n--- Most Aficionado Method ---")
try:
    espresso_aficionado = Customer.most_aficionado(espresso)
    latte_aficionado = Customer.most_aficionado(latte)
    cappuccino_aficionado = Customer.most_aficionado(cappuccino)
    
    print(f"Espresso aficionado: {espresso_aficionado.name if espresso_aficionado else 'None'}")
    print(f"Latte aficionado: {latte_aficionado.name if latte_aficionado else 'None'}")
    print(f"Cappuccino aficionado: {cappuccino_aficionado.name if cappuccino_aficionado else 'None'}")
except Exception as e:
    print(f"Error testing most_aficionado method: {e}")


print("\n--- Error Handling ---")
try:
 
    invalid_customer = Customer("ThisNameIsTooLongForCustomer")
    print("Created invalid customer successfully")
except Exception as e:
    print(f"Expected error for invalid customer name: {e}")

try:
    
    invalid_coffee = Coffee("AB")
    print("Created invalid coffee successfully")
except Exception as e:
    print(f"Expected error for invalid coffee name: {e}")

try:
    
    invalid_order = Order(alice, espresso, 20.0)
    print("Created invalid order successfully")
except Exception as e:
    print(f"Expected error for invalid order price: {e}")