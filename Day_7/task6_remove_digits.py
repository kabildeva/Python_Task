s = input("Enter a string: ")
result = "".join([i for i in s if not i.isdigit()])
print("String without digits:", result)
