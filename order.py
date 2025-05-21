class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.validate_customer(customer)
        self.validate_coffee(coffee)
        self.validate_price(price)
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        Order.all_orders.append(self)
    
    def validate_customer(self, customer):
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
    
    def validate_coffee(self, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee class")
    
    def validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        self.validate_customer(customer)
        self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        self.validate_coffee(coffee)
        self._coffee = coffee
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self.validate_price(price)
        self._price = price