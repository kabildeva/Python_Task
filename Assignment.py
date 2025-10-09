print("\n Assignment Operator Tasks")
print("\n 1.Increment:")
print("\n 2.Decrement:")
print("\n 3.Double:")
print("\n 4.Halve:")
print("\n 5.Remainder:")

choice = int(input("Enter Your Choice 1 to 5: "))
if choice == 1:
    x = int(input("Enter a number: "))
    x += 5
    print("After += 5:", x)

elif choice == 2:
    x = int(input("Enter a number: "))
    x -= 2
    print("After -= 2:", x)

elif choice == 3:
    x = int(input("Enter a number: "))
    x *= 2
    print("After *= 2:", x)

elif choice == 4:
    x = float(input("Enter a number: "))
    x /= 2
    print("After /= 2:", x)

elif choice == 5:
      x = int(input("Enter a number: "))
      x %= 3
      print("After %= 3:", x)

else:
    print("\nWorng choice select between 1 to 5")
