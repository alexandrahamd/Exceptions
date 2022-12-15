import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all.append(Item(row['name'], row['price'], row['quantity']))

    def __str__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv('items.csv')
for item in Item.all:
    print(item)

a = Item("Laptop", 1000, 3)
print(a)
