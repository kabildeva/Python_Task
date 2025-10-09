em = int(input("\n Enter The Salary:"))
ser = int(input(" \n Enter The Service Year:"))

if ser >= 5:
    a = em * 0.05
    b = a + em
    print(" \n Your Salary Pluse Bonus:", b)
else:
    print(" \n Sorry Your Not Eligable for bonus")
