my_dict = {1: "viswa", 2: "name", 3: "return", 4: "mice"}
key = int(input("Enter the key to check: "))
if key in my_dict:
    print("Key already exists")
else:
    print("Key does not exist")
