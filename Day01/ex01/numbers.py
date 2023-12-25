import sys
sys.path.append('..')

from ex00.var import my_var

def my_number():
    with open('my_number.txt', 'w') as file:
        for number in range(1, 101):
            file.write(str(number))
            if number != 100:
                file.write('\n')

if __name__ == '__main__':
    my_var()  # Call my_var function from ex00/var.py
    # my_number()
