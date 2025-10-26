print("\n Combined Operators Tasks ")
print("1. Sum, Difference, Product, Remainder, Floor Division")
print("2. Increment by 5")
print("3. Triple it and check if > 50")
print("4. Check if both numbers > 10 (and)")
print("5. Check if at least one number > 10 (or)")

choice = int(input("\nEnter your choice (1 to 5): "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Remainder:", a % b)
    print("Floor Division:", a // b)

elif choice == 2:
    x = int(input("Enter a number: "))
    x += 5
    print("After increment by 5:", x)

elif choice == 3:
    x = int(input("Enter a number: "))
    x *= 3
    print("Triple value:", x)
    print("Is triple > 50?", x > 50)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Both greater than 10:", (a > 10) and (b > 10))

elif choice == 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("At least one greater than 10:", (a > 10) or (b > 10))

else:
    print("\nWrong choice! Please select between 1 to 5.")
