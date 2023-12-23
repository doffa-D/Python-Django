def my_number():
    with open('numbers.txt','w') as file:
        for number in range(1,101):
            file.write(str(number))
            if number != 100:
                file.write('\n')

if __name__ == '__main__':
    my_number()