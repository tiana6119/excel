# Activity 6 - Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("choose option: ")

    if choice == "5":
        print("Goodbye")
        break

    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))

        if choice == "1":
            print(add(num1, num2))
        elif choice == "2":
            print(subtract(num1, num2))
        elif choice == "3":
            print(multiply(num1, num2))
        elif choice == "4":
            print(divide(num1, num2))
        else:
            print("invalid choice")

    except ValueError:
        print("please enter valid numbers")