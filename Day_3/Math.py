a = int(input("Enter A value : \n"))
b = int(input("Enter B value : \n"))

print("1.Sum \n")
print("2.subraction \n")
print("3.Multipication \n")
print("4.Division \n")

c = int(input("Enter the (1-4) option \n"))
if c == 1:
    print( a + b )
elif c == 2:
    print( a - b )
elif c == 3:
    print(a*b)
elif c == 4:
    print(a/b)
else:
    print("Invalide process")
