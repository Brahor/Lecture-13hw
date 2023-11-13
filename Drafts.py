class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}"

class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product not in self.products:
            self.products[product] = 0
        self.products[product] += quantity

    def update_inventory(self, order):
        for product, quantity in order.items():
            if product in self.products:
                self.products[product] -= quantity
                if self.products[product] < 0:
                    self.products[product] = 0
        self.get_contents()

    def get_contents(self):
        print("Warehouse:")
        for key, value in self.products.items():
            print(f"{key}: {value} remaining")
        print("\n")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.shopping_cart.remove_product(product, quantity)

    def view_cart(self):
        return self.shopping_cart.get_contents()

    def place_order(self, warehouse):
        order = self.shopping_cart.create_order()
        warehouse.update_inventory(order)

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product, quantity):
        if product not in self.cart:
            self.cart[product] = 0
        self.cart[product] += quantity

    def remove_product(self, product, quantity):
        if product in self.cart:
            self.cart[product] -= quantity
            if self.cart[product] <= 0:
                del self.cart[product]

    def get_contents(self):
        print("User's shopping cart:")
        for key, value in self.cart.items():
            print(f"{key}: {value} remaining")
        print("\n")

    def create_order(self):
        return self.cart

# Testing:
product1 = Product("DVD", "Digital Video Dddd", 1000.99)
product2 = Product("Headphones", "Noise-canceling headphones", 189.99)

product1 = Product("Laptop", "High-performance laptop", 999.99)
product2 = Product("Headphones", "Noise-canceling headphones", 149.99)

warehouse = Warehouse()
warehouse.add_product(product1, 10)

warehouse.add_product(product2, 20)

user1 = User("Alice", "alice@example.com")
user1.add_to_cart(product1, 2)
user1.add_to_cart(product2, 3)

warehouse.get_contents()
user1.view_cart()
user1.place_order(warehouse)