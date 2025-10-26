list1 = [1, 2, 3, 4]
list2 = [3, 5, 7, 9]
common = bool(set(list1) & set(list2))
print('Lists have common elements?', common)
