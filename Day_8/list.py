'''#1.Append
name=[]
name.append("7,8,len,9,8")
print(name)

#list using for loop
a= ['apple', 'oringe', 'kiwi', 'strabarry']
for i in a:
    print(i)
    break;

#enter nam
l=[]
count=int(input("enter how many name you want:"))
for i in range(count):
    val=input("enter the name")
    l.append(val)
print(l)

#add number using for loop

b=[1,2,3]
count=int(input("enter the loop:"))
for i in range(count):
    number=int(input("enter the numbers:"))
    b.append(number)
print(b)'''

#5 citys and remove

c = ['madurai', 'chennai', 'karala', 'virudhunagar']
print("Current list:", c)

for i in range(len(c) + 5):  # loop fixed number of times (you can change 5)
    n = input("Enter the name you want to remove (or 'stop' to end): ").lower()
    if n == 'stop':
        break
    if n in c:
        c.remove(n)
        print(f"'{n}' removed. Updated list:", c)
    else:
        print(f"'{n}' not found in list.")

print("Final list:", c)
