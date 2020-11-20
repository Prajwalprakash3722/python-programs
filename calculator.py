# calculator
def add(x, y):
    return x + y


def sub(x, y):
    if x > y:
        return x - y
    else:
        return y - x


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


while True:
    print('''1. Enter "1" for addition.
2. Enter "2" for Subtraction.
3. Enter "3" for Multiplication.
4. Enter "4" for Division.
''')
    choice = input("Enter choice(1/2/3/4): ")
    if choice == '1':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"solution: {add(num1, num2)}")
    elif choice == '2':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"solution: {sub(num1, num2)}")
    elif choice == '3':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"solution: {mul(num1, num2)}")
    elif choice == '4':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"solution: {div(num1, num2)}")
    else:
        print("You have entered the wrong Choice, please review it.")
