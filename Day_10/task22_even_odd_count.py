nums = {1, 2, 3, 4, 5, 6}
even = len([n for n in nums if n % 2 == 0])
odd = len([n for n in nums if n % 2 != 0])
print('Even numbers:', even)
print('Odd numbers:', odd)
