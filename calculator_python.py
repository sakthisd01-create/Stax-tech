# ---------------------------------------------------------
# 🧮 PROJECT 2 : SIMPLE CALCULATOR
# Developed by: [Your Name]
# Description : A stylish, interactive calculator using Python
# ---------------------------------------------------------

import os
import time

# Function to display a nice header
def show_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("🧠  WELCOME TO THE PYTHON CALCULATOR  🧮".center(50))
    print("="*50)
    print()

# Function to perform operations
def calculate():
    while True:
        show_header()
        print("Select an operation:")
        print("1️⃣  Addition")
        print("2️⃣  Subtraction")
        print("3️⃣  Multiplication")
        print("4️⃣  Division")
        print("5️⃣  Exit")
        print("-"*50)

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '5':
            print("\n✨ Thank you for using the calculator! ✨")
            break

        if choice not in ['1', '2', '3', '4']:
            print("\n❌ Invalid choice! Try again...")
            time.sleep(1.5)
            continue

        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\n⚠️ Please enter valid numbers!")
            time.sleep(1.5)
            continue

        if choice == '1':
            result = num1 + num2
            op = '+'
        elif choice == '2':
            result = num1 - num2
            op = '-'
        elif choice == '3':
            result = num1 * num2
            op = '×'
        elif choice == '4':
            if num2 == 0:
                print("\n🚫 Division by zero is not allowed!")
                time.sleep(1.5)
                continue
            result = num1 / num2
            op = '÷'

        print("\n🧾 RESULT:")
        print(f"   {num1} {op} {num2} = {round(result, 3)}")
        print("-"*50)

        again = input("\n🔁 Do you want to perform another operation? (y/n): ").lower()
        if again != 'y':
            print("\n💡 Exiting Calculator... Have a great day! 💫")
            break
        time.sleep(1)

# Run the program
if __name__ == "__main__":
    calculate()
