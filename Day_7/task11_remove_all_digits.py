text = input("Enter a string: ")
result = "".join([ch for ch in text if not ch.isdigit()])
print("String without digits:", result)
