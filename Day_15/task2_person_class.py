from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # format YYYY-MM-DD

    def age(self):
        birth = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")
p = Person(name, country, dob)
print(p.name, "is", p.age(), "years old")
