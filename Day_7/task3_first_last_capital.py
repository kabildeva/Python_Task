s = input("Enter a string: ")
if len(s) > 1:
    s = s[0].upper() + s[1:-1] + s[-1].upper()
else:
    s = s.upper()
print("Modified string:", s)
