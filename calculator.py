def add():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("Error: Invalid numeric input provided.")
def multiply():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    except ValueError:
        print("Error: Invalid numeric input provided.")
def divide():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    except ValueError:
        print("Error: Invalid numeric input provided.")
def main():
    while True:
        print("\n==============================")
        print("   CALCULATOR MASTER MENU     ")
        print("==============================")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[5] Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
         divide()
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
