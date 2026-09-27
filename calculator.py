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
            print("Addition feature coming soon...")
        elif choice == '2':
            print("Subtraction feature coming soon...")
        elif choice == '3':
            print("Multiplication feature coming soon...")
        elif choice == '4':
            print("Division feature coming soon...")
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
