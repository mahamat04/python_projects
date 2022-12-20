def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("A: addition")
print("B: subtraction")
print("C: multiplication")
print("D: division")
print("E: Exit")

while True:
    choice = input('Enter your choice: ')
    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Enter first number: '))
        b = int(input('Enter first number: '))
        print(str(a) + ' + ' + str(b) + ' = ' + str(add(a,b)) + '\n')
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Enter first number: '))
        b = int(input('Enter first number: '))
        print(str(a) + ' - ' + str(b) + ' = ' + str(sub(a,b)) + '\n')
    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Enter first number: '))
        b = int(input('Enter first number: '))
        print(str(a) + ' * ' + str(b) + ' = ' + str(mul(a,b)) + '\n')
    elif choice =='d' or choice == 'D':
        print('Division')
        a = int(input('Enter first number: '))
        b = int(input('Enter first number: '))
        try:
            print(str(a) + ' / ' + str(b) + ' = ' + str(div(a,b)) + '\n')
        except:
            print('Division by zero isn\'t possible\n')
    elif choice == 'e' or choice == 'E':
        print('Program ended')
        quit()