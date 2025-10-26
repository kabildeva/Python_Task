a = input("Enter your Name: ")
name = "kabilan"
Mailid = "kabildeva8@gmail.com"
password = "kabilan"

if a == name:
    print("Valid Name\n")
    c = input("Enter Mail ID: ")
    if c == Mailid:
        print("Valid Mail ID\n")
        d = input("Enter the Password: ")
        if d == password:
            print("Valid Password\n")
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Wrong Mail ID")
else:
    print("Wrong Name")
