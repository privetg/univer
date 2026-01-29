# 1. Сравнение двух чисел
a = float(input())
b = float(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("равны")

# 2. Проверка на четность
n = int(input())
print("четное" if n % 2 == 0 else "нечетное")

# 3. Разделение цифр
n = input()
even = [d for d in n if d.isdigit() and int(d) % 2 == 0]
odd = [d for d in n if d.isdigit() and int(d) % 2 != 0]
print("четные:", *even)
print("нечетные:", *odd)

# 4. Проверка на простоту
n = int(input())
if n < 2:
    print("NO")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("NO")
            break
    else:
        print("YES")

# 5. Среднее арифметическое трех чисел
a = float(input())
b = float(input())
c = float(input())
print((a + b + c) / 3)

# 6. Кратность 7
n = int(input())
print("кратно 7" if n % 7 == 0 else "не кратно 7")

# 7. Високосный год
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("високосный")
else:
    print("не високосный")

# 8. Дни в месяце
month = int(input())
if month == 2:
    print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)

# 9. Площадь треугольника по формуле Герона
a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)

# 10. Равенство трех чисел
a = float(input())
b = float(input())
c = float(input())
print("равны" if a == b == c else "не равны")

# 11. Проверка возраста
age = int(input())
if age < 18:
    print("несовершеннолетний")
elif 18 <= age <= 65:
    print("взрослый")
else:
    print("пенсионер")

# 12. Положительное или отрицательное
n = float(input())
if n > 0:
    print("положительное")
elif n < 0:
    print("отрицательное")
else:
    print("ноль")

# 13. Дни в феврале
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(29)
else:
    print(28)

# 14. Принадлежность точки квадрату
x = float(input())
y = float(input())
print("принадлежит" if 0 <= x <= 5 and 0 <= y <= 5 else "не принадлежит")

# 15. Сумма и разность
a = float(input())
b = float(input())
print("Сумма:", a + b)
print("Разность:", a - b)

# 16. Кратность 3 и 5
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("кратно 3 и 5")
elif n % 3 == 0:
    print("кратно 3")
elif n % 5 == 0:
    print("кратно 5")
else:
    print("не кратно")

# 17. Вековой год
year = int(input())
print("вековой" if year % 100 == 0 else "не вековой")

# 18. Целое или дробное
n = float(input())
print("целое" if n == int(n) else "дробное")