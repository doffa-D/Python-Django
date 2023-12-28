# from beverages import HotBeverage

# class CoffeeMachine():
#     def __init__(self):
#         self.count = 0

#     class EmptyCup(HotBeverage):
#         desc = "An empty cup?! Gimme my money back!"
#         def __init__(self):
#             super.__init__(name = "empty cup",price = 0.90)

#     class BrokenMachineException(Exception):

#         def __init__(self):
#             super().__init__(msg = "This coffee machine has to be repaired.")

#     def repair(self):
#         self.count = 0

#     def serve(self):
#         self.count++
#         if self.count > 9
#             raise self.BrokenMachineException()


ascii_decimal = 24

# Convert decimal to hexadecimal and format it as 0xXXXXXXXX
hex_string = f'0x{ascii_decimal:08X}'

print(hex_string)

