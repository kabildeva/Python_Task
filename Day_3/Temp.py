temp = int(input("Enter the Current Temp:"))
if temp < 0:
    print(" Freesing wether")
elif temp >= 0 and temp < 10:
    print(" Very cold wether")
elif temp >= 10 and temp < 20:
    print(" cold wether")
elif temp >= 20 and temp < 30:
    print("Normal Temp")
elif temp >= 30 and temp < 40:
    print(" Hot wether")
elif temp >= 40:
    print(" Very Hot Wether")
else:
    print("The tempracture is not considarable")
