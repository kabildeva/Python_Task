class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"

calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.sub(a, b))
print("Multiplication:", calc.mul(a, b))
print("Division:", calc.div(a, b))
