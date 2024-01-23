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
            prices.append(item['price'])

        self.total_price = sum(prices)

amir_basket = Basket(1111)

amir_basket.add_item({"name": "ASUS N552VW-J", "price": 30, "code": "1010"})
amir_basket.add_item({"name": "ASUS N552VW-A", "price": 32, "code": "2020"})
amir_basket.add_item({"name": "ASUS N552VW-B", "price": 31, "code": "3030"})

print(amir_basket.basket_items)
print(amir_basket.total_price)


amir_basket.remove_item({"name": "ASUS N552VW-J", "price": 30, "code": "1010"})

print(amir_basket.basket_items)
print(amir_basket.total_price)
