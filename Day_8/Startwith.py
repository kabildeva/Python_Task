#1.startwith
name = "kabilan"
print(name.startswith("a"))
#2.endwith
print(name.endswith("ing"))

#3.replace
print(name.replace("a","_"))

#4.find
print(name.find("a"))

#5.isalnum
print(name.isalnum())

#6.for loop
a=''.join([name[i]for i in range(len(name)-1,-1,-1,)])
print(a)
