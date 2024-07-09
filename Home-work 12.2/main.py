class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"

# Створення екземплярів класів Item та User
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5, description: yellow, dimensions: small

buyer = User("Andrii", "Pistrui", "02628162")
print(buyer)  # Andrii Pistrui, phone: 02628162

# Створення замовлення
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
# User: Andrii Pistrui, phone: 02628162
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.

# Перевірка методів
assert isinstance(cart.user, User), 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"

cart.add_item(apple, 10)
print(cart)
# User: Andrii Pistrui, phone: 02628162
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.

assert cart.get_total() == 40, 'Повинно залишатися 40!'
