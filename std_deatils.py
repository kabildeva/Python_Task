name = "kabilan"
year = "2 year"
sem = "1 semaseter"
seb = ["Tamil", "English", "Math", "Computer Science", "Physics"]

a = input(" Enter the Sudent Name or Year:\n")

if a == name:
    print(name, "\n", year, "\n", sem, "\n ***Subjects***\n", seb)
elif a == year:
    print(name)
    b = input(" \n Enter The Name:")
    if b == name:
        print(name, "\n", year, "\n", sem, "\n ***Subjects***\n", seb)
    else:
        print("\n Wrong Name")
else:
    print("Please Enter Valid Student Name")
