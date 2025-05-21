class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.validate_name(name)
        self._name = name
        Customer.all_customers.append(self)
    
    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self.validate_name(name)
        self._name = name
    
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
    
    def coffees(self):
        
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
        
        
        customer_spending = {}
        
        from order import Order
        coffee_orders = [order for order in Order.all_orders if order.coffee == coffee]
        
        if not coffee_orders:
            return None
        
        for order in coffee_orders:
            customer = order.customer
            if customer in customer_spending:
                customer_spending[customer] += order.price
            else:
                customer_spending[customer] = order.price
        
        return max(customer_spending, key=customer_spending.get)