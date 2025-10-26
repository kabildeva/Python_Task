def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

nums = {6, 10, 28, 12}
perfect_nums = [n for n in nums if is_perfect(n)]
print('Perfect numbers:', perfect_nums)
