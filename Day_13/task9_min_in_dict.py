my_dict = {"a": 10, "b": 3, "c": 15}
values = list(my_dict.values())
minimum = values[0]
for v in values:
    if v < minimum:
        minimum = v
print("Minimum value in dictionary:", minimum)
