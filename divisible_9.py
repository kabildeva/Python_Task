count = 0
sum = 0
for i in range(100, 201):
    if i % 9 == 0:
        print(i)
        count += 1
        sum += i
print("Count:", count)
print("Sum:", sum)