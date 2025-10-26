n = int(input("Enter number of terms: "))
sum = 0
for i in range(1, n + 1):
    print(f"1/{i}", end="  ")
    sum += 1 / i
print("\nSum of harmonic series:", round(sum, 3))