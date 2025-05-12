class Menu_item:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.total_price():,.2f}"


class Beer(Menu_item):
    def __init__(self, brand: str, price: float, quantity: int = 1):
        super().__init__(name=brand, price=price, quantity=quantity)
        self.brand = brand

    def beer_discount(self):
        if self.quantity % 6 == 0:
            return self.total_price() * 0.9
        else:
            return self.total_price()
        
    def __repr__(self):
        return f"Beer {self.name} - x{self.quantity} ${self.beer_discount():,.2f}"


class Juice(Menu_item):
    def __init__(self, flavor: str, price: float, quantity: int = 1):
        super().__init__(name=flavor, price=price, quantity=quantity)

    def juice_discount(self):
        if self.total_price() > 30000:
            return self.total_price() * 0.95
        else:
            return self.total_price()

    def __repr__(self):
        return f"Juice Flavor {self.name} - x{self.quantity} ${self.juice_discount():,.2f}"


class Dessert(Menu_item):
    def __init__(self, name: str, price: float, quantity: int = 1):
        super().__init__(name=name, price=price, quantity=quantity)

    def dessert_discount(self):
        if self.name == "Chocolate Cake":
            return self.total_price() * 0.5
        else:
            return self.total_price()

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.dessert_discount():,.2f}"


class Coffee(Menu_item):
    def __init__(self, style: str, price: float, quantity: int = 1):
        super().__init__(name=style, price=price, quantity=quantity)

    def coffee_discount(self):
        if self.quantity >= 3:
            return self.total_price() * 0.85
        else:
            return self.total_price()

    def __repr__(self):
        return f"Coffee {self.name} - x{self.quantity} ${self.coffee_discount():,.2f}"


class Sandwich(Menu_item):
    def __init__(self, type_: str, price: float, quantity: int = 1):
        super().__init__(name=type_, price=price, quantity=quantity)

    def __repr__(self):
        return f"Sandwich {self.name} - x{self.quantity} ${self.total_price():,.2f}"


class Pizza(Menu_item):
    def __init__(self, size: str, price: float, quantity: int = 1):
        super().__init__(name=f"{size} Pizza", price=price, quantity=quantity)

    def pizza_discount(self):
        if "Large" in self.name and self.quantity >= 2:
            return self.total_price() * 0.8
        else:
            return self.total_price()

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.pizza_discount():,.2f}"


class Salad(Menu_item):
    def __init__(self, kind: str, price: float, quantity: int = 1):
        super().__init__(name=kind, price=price, quantity=quantity)

    def __repr__(self):
        return f"Salad {self.name} - x{self.quantity} ${self.total_price():,.2f}"


class Water(Menu_item):
    def __init__(self, size: str, price: float, quantity: int = 1):
        super().__init__(name=f"Water {size}", price=price, quantity=quantity)

    def water_discount(self):
        if self.quantity >= 10:
            return self.total_price() * 0.9
        else:
            return self.total_price()

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.water_discount():,.2f}"


class IceCream(Menu_item):
    def __init__(self, flavor: str, price: float, quantity: int = 1):
        super().__init__(name=f"Ice Cream ({flavor})", price=price, quantity=quantity)

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.total_price():,.2f}"


class Soup(Menu_item):
    def __init__(self, variety: str, price: float, quantity: int = 1):
        super().__init__(name=f"{variety} Soup", price=price, quantity=quantity)

    def soup_discount(self):
        if self.quantity > 5:
            return self.total_price() * 0.95
        else:
            return self.total_price()

    def __repr__(self):
        return f"{self.name} - x{self.quantity} ${self.soup_discount():,.2f}"


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
            elif isinstance(item, Coffee):
                total += item.coffee_discount()
            elif isinstance(item, Pizza):
                total += item.pizza_discount()
            elif isinstance(item, Water):
                total += item.water_discount()
            elif isinstance(item, Soup):
                total += item.soup_discount()
            else:
                total += item.total_price()
        return total

    def show_order(self):
        print("Order summary:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():,.2f}")

