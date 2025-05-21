# Coffee Shop Domain Modeling

This project implements a domain model for a Coffee Shop using object-oriented programming in Python. The model consists of three main entities: `Customer`, `Coffee`, and `Order`, with relationships between them.

## Project Structure


coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── debug.py

## Domain Model

### Relationships
- A `Customer` can place many `Orders`
- A `Coffee` can have many `Orders`
- An `Order` belongs to one `Customer` and one `Coffee`
- The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity

### Classes

#### Customer Class
- Initializes with a name (string between 1 and 15 characters)
- Methods:
  - `orders()`: Returns all orders made by the customer
  - `coffees()`: Returns unique list of coffees ordered by the customer
  - `create_order(coffee, price)`: Creates a new order for the customer
  - `most_aficionado(coffee)`: Class method that returns the customer who spent the most on a specific coffee

#### Coffee Class
- Initializes with a name (string, at least 3 characters long)
- Methods:
  - `orders()`: Returns all orders for this coffee
  - `customers()`: Returns unique list of customers who ordered this coffee
  - `num_orders()`: Returns the total number of times this coffee was ordered
  - `average_price()`: Returns the average price of this coffee based on its orders

#### Order Class
- Initializes with a customer instance, a coffee instance, and a price (float between 1.0 and 10.0)
- Properties:
  - `customer`: Returns the customer instance for the order
  - `coffee`: Returns the coffee instance for the order
  - `price`: Returns the price of the order

## Setup and Running

1. Create a virtual environment:
```bash
pipenv install
pipenv shell
```

2. Install dependencies:
```bash
pipenv install pytest
```

3. Run the debug script:
```bash
python debug.py


