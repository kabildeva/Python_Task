aptitude = int(input("Enter Aptitude marks: "))
gd = int(input("Enter GD marks: "))
technical = int(input("Enter Technical marks: "))
hr = int(input("Enter HR marks: "))

if aptitude >= 85:
    print("\nAptitude Passed")
else:
    print("\nAptitude Fail")
    print("Sorry, you are not eligible for this job")
    exit()

if gd >= 90:
    print("GD Eligible")
else:
    print("GD Fail")
    print("Sorry, you are not eligible for this job")
    exit()

if technical >= 80:
    print("Technical Round Passed")
else:
    print("Technical Round Fail")
    print("Sorry, you are not eligible for this job")
    exit()

if hr >= 95:
    print("HR Round Passed")
else:
    print("HR Round Fail")
    print("Sorry, you are not eligible for this job")
    exit()
    
total = aptitude + gd + technical + hr
print(f"\nTotal Marks: {total}")
if 390 <= total <= 400:
    print("Your Salary is 30,000")
elif 380 <= total < 390:
    print("Your Salary is 28,000")
elif 370 <= total < 380:
    print("Your Salary is 25,000")
elif 350 <= total < 370:
    print("Your Salary is 20,000")
else:
    print("Sorry, your total marks are not enough for salary allocation")
