original = {"a": 1, "b": 2, "c": 3}
keys = ["a", "c"]
new_dict = {k: original[k] for k in keys}
print(new_dict)
