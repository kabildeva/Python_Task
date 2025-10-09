print("\n Logical Operator Tasks ")
print("1. a and b")
print("2. a or b")
print("3. not a")
print("4. (a and b) or c")
print("5. (not a) and b")

choice = int(input("\nEnter your choice (1 to 5): "))

if choice == 1:
    a = input("Enter first boolean (True/False): ") == "True"   
    b = input("Enter second boolean (True/False): ") == "True"
    print("Result of a and b:", a and b)

elif choice == 2:
    a = input("Enter first boolean (True/False): ") == "True"
    b = input("Enter second boolean (True/False): ") == "True"
    print("Result of a or b:", a or b)

elif choice == 3:
    a = input("Enter boolean (True/False): ") == "True"
    print("Result of not a:", not a)

elif choice == 4:
    a = input("Enter first boolean (True/False): ") == "True"
    b = input("Enter second boolean (True/False): ") == "True"
    c = input("Enter third boolean (True/False): ") == "True"
    print("Result of (a and b) or c:", (a and b) or c)

elif choice == 5:
    a = input("Enter first boolean (True/False): ") == "True"
    b = input("Enter second boolean (True/False): ") == "True"
    print("Result of (not a) and b:", (not a) and b)

else:
    print("\nWrong choice! Please select between 1 to 5.")
