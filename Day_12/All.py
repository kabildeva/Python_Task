'''#-------1.Task--------


def lo(**a):
    for i in a.keys():
        print("key",i)
lo(a=1,b=5,c=9)

#------2.Task--------

print("\n")
def kk(**a):
    for i in a.values():
        print("Valuse",i)
kk(a=2,b=55,c=66)

#-----3.Task--------

def pp(**a):
    b=0
    for i in a.values():
        b += i
        print("sum",b)
pp(a=int(input("Enter the a value:"))
   ,b=int(input("Enter the b value:"))
   ,c=int(input("Enter the c value:"))
   ,d=int(input("Enter the d value:")))'''
#-----4.Task------

def hh(**a):
    even=0
    for i in a.values():
        if i%2==0:
            even+=i
    print("Even values:",even)

hh(a=int(input("Enter the avalue:"))
   ,b=int(input("Enter the b value:"))
   ,c=int(input("Enter the c value:"))
   ,d=int(input("Enter the d value:")))



#---------5.Task--------------

def perfect_number(*a):
    for n in a:
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 = sum1 + i
        if sum1 == n:
            print(n, "is a Perfect Number")
        else:
            print(n, "is not a Perfect Number")

perfect_number(6, 28, 12)
print()

#---------6.Task--------------

def remove_last(**a):
    print("Before remove:", a)
    a.popitem()
    print("After remove:", a)

remove_last(a=10, b=20, c=30)
print()

#---------7.Task--------------

def calculator(a, b, op):
    if op == '+':
        print("Addition is:", a + b)
    elif op == '-':
        print("Subtraction is:", a - b)
    elif op == '*':
        print("Multiplication is:", a * b)
    elif op == '/':
        print("Division is:", a / b)
    else:
        print("Invalid operator")

calculator(10, 5, '+')
calculator(10, 5, '*')
print()

#---------8.Task--------------

def palindrome(a):
    if a == a[::-1]:
        print(a, "is Palindrome")
    else:
        print(a, "is not Palindrome")

palindrome("madam")
palindrome("hello")
print()

#----------9.Task-------------

def count_string(a):
    v = c = s = 0
    for ch in a:
        if ch.lower() in "aeiou":
            v = v + 1
        elif ch.isalpha():
            c = c + 1
        else:
            s = s + 1
    print("Vowels:", v)
    print("Consonants:", c)
    print("Special Characters:", s)

count_string("Hello@123")


