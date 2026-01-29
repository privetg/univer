import math

# Задача 1
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
s = (2 * math.cos(x - 2/3)) / (0.5 + math.sin(y)**2) * (1 + z**2 / (3 - z**2/5))
print(round(s, 6))

# Задача 2
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
s = ((9 + (x - y)**2)**(1/3)) / (x**2 + y**2 + 2) - math.exp(abs(x - y)) * math.tan(z)**3
print(round(s, 6))