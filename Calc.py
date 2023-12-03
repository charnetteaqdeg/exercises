import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of a negative number"

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Error: Cannot calculate factorial of a negative number"

def main():
    while True:
        print("\n=== Console Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Factorial (x!)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in {'1', '2', '3', '4', '5'}:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Result:", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result:", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result:", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("Result:", result)
            elif choice == '5':
                result = power(num1, num2)
                print("Result:", result)

        elif choice in {'6', '7'}:
            num = float(input("Enter the number: "))

            if choice == '6':
                result = square_root(num)
                print("Result:", result)
            elif choice == '7':
                result = factorial(int(num))
                print("Result:", result)

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
