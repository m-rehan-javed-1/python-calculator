print("Welcome to Python Calculator")
def calculator():
    print()        #Just for blank line
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero "
    else:
        result = "Error: Invalid choice "
    print()
    print("Result:", result)

while True:        # Method to run infinite times.
    calculator()
    repeat = input("Do you want to continue? (y/n): ")
    if repeat != "y":

        break
