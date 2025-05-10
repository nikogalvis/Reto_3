class Menu_item:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price*self.quantity
    
    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.total_price()}"

class Beer(Menu_item):
    def __init__(self, brand: str, price: float, quantity: int = 1):
        super().__init__(name = brand, price = price, quantity = quantity)
        self.brand = brand

    def beer_discount(self): #* There is a Discount for buy a sixpack
        if(self.quantity%6 == 0):
            return self.total_price() - ((self.total_price())*(0.1))
        else:
            return self.total_price()
        
    def __repr__(self):
        return f"Beer {self.name} - x{self.quantity} ${self.beer_discount()}"
    
class Juice(Menu_item):
    def __init__(self, flavor: str, price: float, quantity: int = 1):
        super().__init__(name = flavor, price = price, quantity = quantity)
        self.brand = flavor
    
    def juice_discount(self): 
    #* Thanks to a sponsorship, purchases of 30k or more have a 5% Discount
        if(self.total_price() > 30000):
            return self.total_price() - ((self.total_price())*(0.05))
        else:
            return self.total_price()

    def __repr__(self):
        return f"Juice Flavor {self.name} - x{self.quantity} ${self.juice_discount()}"

class Dessert(Menu_item):
    def __init__(self, name: str, price: float, quantity: int = 1):
        super().__init__(name = name, price = price, quantity = quantity)
    
    def dessert_discount(self): #There is an excedent of chocolate cakes, so 50% discount!
        if(self.name == "Chocolate Cake"):
            return (self.total_price())*0.5
        else:
            return self.total_price()

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.dessert_discount()}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: Menu_item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            if isinstance(item, Beer):
                total += item.beer_discount()
            elif isinstance(item, Juice):
                total += item.juice_discount()
            elif isinstance(item, Dessert):
                total += item.dessert_discount()
            else:
                total += item.total_price()
        return total

    def show_order(self):
        print("Order summary:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():,.2f}")


data_1 = Beer(brand = "Poker", price = 2500, quantity = 4)
data_2 = Juice(flavor = "Apple", price = 3200, quantity = 10)
data_3 = Dessert(name = "Apple Pie", price = 20000, quantity = 1)
print(data_1.__repr__())
print(data_2.__repr__())
print(data_3.__repr__())
