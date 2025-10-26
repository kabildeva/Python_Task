#-------Task no 1 & 2------------

'''from datetime import datetime as d
x=d.now()
y=x.timetuple()
print("Time tuple: ",y)
print("Date: ",y[2],y[1],y[0])
print("Time: ",y[3],y[4],y[5])
print("Week numer of the Year: ",x.strftime("%U"))
print("Week day of week: ",x.strftime("%w"))
print("Day of year: ",x.strftime("%j"))
print("Day of month",y[2])
print("Day of week",y[6])
a=int(input("enter the year you want to check:"))
check=a%4
if check == 0:
    print("The given year is a leap year")
else:
    print("it's not a leap year")'''
#--------Task no 3---------

'''from datetime import datetime as d

x=int(input("Enter the date:"))
y=input("Enter the Month:")
z=int(input("Enter the year:"))

date=f"{x} {y} {z}"

print("Date",d.strptime(date,"%d %B %Y"))'''


