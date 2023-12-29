from beverages import HotBeverage, Coffee, Tea, Cappuccino
import random

class CoffeeMachine():
    def __init__(self):
        self.count = 0

    class EmptyCup(HotBeverage):
        desc = "An empty cup?! Gimme my money back!"
        def __init__(self):
            super().__init__(name="empty cup", price=0.90)

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.count = 0

    def serve(self, Klass):
        self.count += 1
        if self.count > 9:
            raise self.BrokenMachineException()
        return Klass() if random.randint(0, 1) == 0 else self.EmptyCup()

if __name__ == "__main__":
    for i in range(2):
        try:
            machine = CoffeeMachine()

            print(machine.serve(HotBeverage))
            print(machine.serve(Coffee))
            print(machine.serve(Coffee))
            print(machine.serve(Coffee))
            print(machine.serve(Tea))
            print(machine.serve(Tea))
            print(machine.serve(Cappuccino))
            print(machine.serve(Coffee))
            print(machine.serve(Tea))
            print(machine.serve(Tea))
            print(machine.serve(Cappuccino))
        except Exception as e:
            print(e)
            machine.repair()
