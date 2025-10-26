def task_1():
    fruits = ["apple", "banana", "mango", "grape", "orange"]
    print(fruits)

def task_2():
    fruits = ["apple", "banana", "mango", "grape", "orange"]
    fruits.append("pineapple")
    fruits.remove("banana")
    print(fruits)

def task_3():
    numbers = [10, 50, 20, 80, 30]
    print("Max:", max(numbers))
    print("Min:", min(numbers))

def task_4():
    numbers = [5, 2, 8, 1, 9]
    numbers.sort()
    print(numbers)

def task_5():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)

def task_6():
    cities = ["Madurai", "Chennai", "Salem", "Erode", "Trichy"]
    for city in cities:
        print(city)

def task_7():
    nums = [10, 20, 30, 40, 50]
    total = 0
    for n in nums:
        total += n
    print("Sum =", total)

def task_8():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    print("Even numbers:", count)

def task_9():
    nums = [1, 2, 3, 4, 5]
    for n in nums:
        print(n ** 2)

def task_10():
    nums = [10, 20, 30, 40, 50]
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])

# ------------------- Tuple Tasks -------------------

def task_11():
    colors = ("red", "green", "blue", "yellow", "pink")
    print(colors)

def task_12():
    t = (10, 20, 30, 40, 50)
    print(t[0], t[-1])

def task_13():
    t = (5, 10, 15, 20)
    print("Length:", len(t))

def task_14():
    t = (10, 20, 25, 30, 35)
    print(25 in t)

def task_15():
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    print(t1 + t2)

def task_16():
    t = (1, 2, 3, 2, 4, 2, 5)
    print("Index of 2:", t.index(2))
    print("Count of 2:", t.count(2))

def task_17():
    t = (1, 2, 3, 4)
    lst = list(t)
    lst.append(5)
    print(lst)

def task_18():
    t = (10, 20, 30, 40, 50, 60)
    print(t[1:4])

def task_19():
    fruits = ('Apple', 'Banana', 'Cherry')
    a, b, c = fruits
    print(a, b, c)

def task_20():
    t = (1, 2, (3, 4, 5))
    print("Main tuple:", t)
    print("Nested tuple:", t[2])

# ---------------- Tuple with Loops -----------------

def task_21():
    t = (5, 10, 15, 20, 25)
    for x in t:
        print(x)

def task_22():
    t = (1, 2, 3, 4, 5)
    total = 0
    for n in t:
        total += n
    print("Sum =", total)

def task_23():
    t = ('A', 'B', 'C', 'D')
    for ch in t:
        print(ch)

def task_24():
    t = (10, 11, 12, 13, 14, 15)
    for n in t:
        if n % 2 == 0:
            print(n)

def task_25():
    t = (1, 2, 3, 4, 5, 6, 7)
    count = 0
    for n in t:
        if n % 2 != 0:
            count += 1
    print("Odd count =", count)

def task_26():
    t = (45, 12, 89, 33, 67)
    small = t[0]
    for n in t:
        if n < small:
            small = n
    print("Smallest =", small)

def task_27():
    t = (2, 3, 4, 5)
    product = 1
    for n in t:
        product *= n
    print("Product =", product)

def task_28():
    t = ('apple', 'banana', 'grapes')
    for word in t:
        print(word.upper())

def task_29():
    t = ('a', 'b', 'e', 'f', 'i', 'o', 'u')
    vowels = 'aeiou'
    count = 0
    for ch in t:
        if ch in vowels:
            count += 1
    print("Vowel count =", count)

def task_30():
    t = (100, 200, 300, 400)
    for i in range(len(t)):
        print("Index:", i, "Value:", t[i])
# ---------------- Tuple with while -----------------
while True:
    print("\n📘 Python List & Tuple Tasks")
    print("1–10 ➜ List Tasks (Without / With Loop)")
    print("11–30 ➜ Tuple Tasks (Without / With Loop)")
    print("0 ➜ Exit")
    choice = int(input("\nEnter task number (0–30): "))

    if choice == 0:
        print("Exiting... 👋")
        break
    elif 1 <= choice <= 30:
        globals()[f"task_{choice}"]()
    else:
        print("❌ Invalid task number! Try again.")
