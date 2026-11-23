print("===== SIMPLE CALCULATOR =====")

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an operation (1-4): ")

if choice == "1":
    print("Result:", n1 + n2)
elif choice == "2":
    print("Result:", n1 - n2)
elif choice == "3":
    print("Result:", n1 * n2)
elif choice == "4":
    if n2 != 0:
        print("Result:", n1 / n2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid choice.")
