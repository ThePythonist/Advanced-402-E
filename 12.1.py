class Product:
    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code


class Basket:
    def __init__(self, id):
        self.basket_items = []
        self.total_price = 0
        self.id = id
        self.count = len(self.basket_items)

    def add_item(self, product):
        if product not in self.basket_items:
            self.basket_items.append(product)

        self.calculate_total_price()

    def remove_item(self, product):
        if product in self.basket_items:
            self.basket_items.remove(product)

        self.calculate_total_price()

    def calculate_total_price(self):
        prices = []
        for item in self.basket_items:
            prices.append(item.price)

        self.total_price = sum(prices)


# Create instances of Product
product1 = Product("ASUS N552VW-J", 30, "1010")
product2 = Product("ASUS N552VW-A", 32, "2020")
product3 = Product("ASUS N552VW-B", 31, "3030")

# Create instance of Basket
amir_basket = Basket(1111)

# Add products to the basket
amir_basket.add_item(product1)
amir_basket.add_item(product2)
amir_basket.add_item(product3)

# Print basket items and total price
print("Basket Items:", [i.name for i in amir_basket.basket_items])
print("Total Price:", amir_basket.total_price)

# Remove a product from the basket
amir_basket.remove_item(product1)

# Print basket items and total price after removal
print("Basket Items:", [i.name for i in amir_basket.basket_items])
print("Total Price:", amir_basket.total_price)
