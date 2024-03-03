class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name":name, "price":price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0

        for item in self.items:
            total += item['price']
        
        # then return total

        # A better way to do this though...dictionary comprehension
        return sum([item['price'] for item in self.items])
        
        
        
mystore = Store("chimera")
mystore.add_item("pencil", 15)
mystore.add_item("pen", 20)

print(mystore.stock_price())
# print(mystore.items)


