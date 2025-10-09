print("Arithmetic Operator Menu")
print("1. Find Sum of Two Numbers")
print("2. Find Product of Two Numbers")
print("3. Find Square of a Number")
print("4. Find Cube of a Number")
print("5. Find Remainder of Division")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product:", a * b)

elif choice == 3:
    a = int(input("Enter a number: "))
    print("Square:", a ** 2)

elif choice == 4:
    a = int(input("Enter a number: "))
    print("Cube:", a ** 3)

elif choice == 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Remainder:", a % b)

else:
    print("Invalid choice! Please choose between 1 to 5.")
