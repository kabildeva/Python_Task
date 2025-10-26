names = {'Arun', 'Kumar', 'Deva'}
vowels = 'aeiouAEIOU'
for name in names:
    count = sum(1 for c in name if c in vowels)
    print(f'{name}: {count} vowels')
