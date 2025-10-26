matrix = [
    [1, 2],
    [3, 4]
]

total = 0
for i in range(2):
    for j in range(2):
        total += matrix[i][j]

print("Sum of all elements:", total)
