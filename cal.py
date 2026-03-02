import math

def add(x, y):
    """Perform addition"""
    return x + y

def subtract(x, y):
    """Perform subtraction"""
    return x - y

def multiply(x, y):
    """Perform multiplication"""
    return x * y

def divide(x, y):
    """Perform division"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Perform exponentiation"""
    return x ** y

def modulo(x, y):
    """Perform modulo operation"""
    if y == 0:
        return "Error! Cannot perform modulo with zero."
    return x % y

def square_root(x):
    """Calculate square root"""
    if x < 0:
        return "Error! Cannot calculate square root of negative number."
    return math.sqrt(x)

def factorial(x):
    """Calculate factorial"""
    if x < 0 or x != int(x):
        return "Error! Factorial requires a non-negative integer."
    return math.factorial(int(x))

def sine(x):
    """Calculate sine (x in degrees)"""
    return math.sin(math.radians(x))

def cosine(x):
    """Calculate cosine (x in degrees)"""
    return math.cos(math.radians(x))

def tangent(x):
    """Calculate tangent (x in degrees)"""
    return math.tan(math.radians(x))

def logarithm(x, base=10):
    """Calculate logarithm"""
    if x <= 0:
        return "Error! Logarithm undefined for non-positive numbers."
    return math.log(x, base)

def percentage(x, y):
    """Calculate percentage (y% of x)"""
    return (y / 100) * x

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("           ADVANCED CALCULATOR")
    print("="*50)
    print("Basic Operations:")
    print("  1. Add         (+)          6. Modulo    (%)")
    print("  2. Subtract    (-)          7. Power     (^)")
    print("  3. Multiply    (*)          8. Percentage")
    print("  4. Divide      (/)          9. Factorial (!)")
    print("  5. Square Root (√)")
    print("\nScientific Functions:")
    print("  10. Sine       (sin)")
    print("  11. Cosine     (cos)")
    print("  12. Tangent    (tan)")
    print("  13. Logarithm  (log)")
    print("  14. Exit")
    print("="*50)

def get_choice():
    """Get valid operation choice from user"""
    while True:
        choice = input("\nEnter choice (1-14): ").strip()
        if choice in [str(i) for i in range(1, 15)]:
            return choice
        print("❌ Invalid choice! Please enter a number between 1 and 14.")

def get_number(prompt):
    """Get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = get_choice()

        if choice == '14':
            print("\n👋 Thank you for using the calculator. Goodbye!")
            break

        # Operations requiring two numbers
        if choice in ['1', '2', '3', '4', '6', '7', '8']:
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")

            if choice == '1':
                print(f"\n✓ Result: {x} + {y} = {add(x, y)}")
            elif choice == '2':
                print(f"\n✓ Result: {x} - {y} = {subtract(x, y)}")
            elif choice == '3':
                print(f"\n✓ Result: {x} × {y} = {multiply(x, y)}")
            elif choice == '4':
                result = divide(x, y)
                print(f"\n✓ Result: {x} ÷ {y} = {result}")
            elif choice == '6':
                result = modulo(x, y)
                print(f"\n✓ Result: {x} % {y} = {result}")
            elif choice == '7':
                print(f"\n✓ Result: {x} ^ {y} = {power(x, y)}")
            elif choice == '8':
                result = percentage(x, y)
                print(f"\n✓ Result: {y}% of {x} = {result}")

        # Operations requiring one number
        elif choice in ['5', '9', '10', '11', '12', '13']:
            x = get_number("Enter number: ")

            if choice == '5':
                result = square_root(x)
                print(f"\n✓ Result: √{x} = {result}")
            elif choice == '9':
                result = factorial(x)
                print(f"\n✓ Result: {int(x)}! = {result}")
            elif choice == '10':
                result = sine(x)
                print(f"\n✓ Result: sin({x}°) = {result:.6f}")
            elif choice == '11':
                result = cosine(x)
                print(f"\n✓ Result: cos({x}°) = {result:.6f}")
            elif choice == '12':
                result = tangent(x)
                print(f"\n✓ Result: tan({x}°) = {result:.6f}")
            elif choice == '13':
                while True:
                    try:
                        base = input("Enter logarithm base (default 10): ").strip()
                        if base == "":
                            base = 10
                        else:
                            base = float(base)
                        break
                    except ValueError:
                        print("❌ Invalid base! Please enter a valid number.")
                result = logarithm(x, base)
                print(f"\n✓ Result: log_{base}({x}) = {result:.6f}")