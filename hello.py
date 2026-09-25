def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "На ноль делить нельзя!"
    return a / b

def power(a, b):
    return a ** b



print("Простой калькулятор")
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
print("20 / 5 =", divide(20, 5))
print("8 / 0 =", divide(8, 0))
print("2 в степени 10 =", power(2, 10))