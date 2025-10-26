import math
n = int(input("Enter n: "))
r = int(input("Enter r: "))
n_fact = math.factorial(n)
r_fact = math.factorial(r)
nr_fact = math.factorial(n - r)
combination = n_fact // (r_fact * nr_fact)
print(f"C({n},{r}) =", combination)
