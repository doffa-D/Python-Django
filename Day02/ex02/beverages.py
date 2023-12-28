class HotBeverage:
    desc = "Just some hot water in a cup."
    def __init__(self , name = "hot beverage",price = 0.30):
        self.name = name
        self.price = price

    def description(self):
        return self.desc

    def __str__(self):
        return f"name: {self.name}\nprice: {self.price}\ndescription: {self.description()}"


class Coffee(HotBeverage):
    desc = "A coffee, to stay awake."
    def __init__(self):
        super().__init__(name = "coffee", price = 0.40)

class Tea(HotBeverage):
    desc = "Just some hot water in a cup."
    def __init__(self):
        super().__init__(name = "Tea", price = 0.30)

class Chocolate(HotBeverage):
    desc = "Chocolate, sweet chocolate..."
    def __init__(self):
        super().__init__(name = "chocolate", price = 0.50)

class Cappuccino(HotBeverage):
    desc = "Un po’ di Italia nella sua tazza!"
    def __init__(self):
        super().__init__(name = "cappuccino", price = 0.45)




x = Coffee()
print(x.__str__())
print("================================")
x = Tea()
print(x.__str__())
print("================================")
x = Chocolate()
print(x.__str__())
print("================================")
x = Cappuccino()
print(x.__str__())

