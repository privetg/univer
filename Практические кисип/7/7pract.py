import math

# Вариант 0
def area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
a1, b1, c1 = float(input()), float(input()), float(input())
a2, b2, c2 = float(input()), float(input()), float(input())
a3, b3, c3 = float(input()), float(input()), float(input())
if area(a1, b1, c1) == area(a2, b2, c2) == area(a3, b3, c3):
    print("равновеликие")
else:
    print("не равновеликие")

# Вариант 1
def circle(r): return math.pi * r * r
def rect(a, b): return a * b
def triangle(b, h): return 0.5 * b * h
choice = int(input())
if choice == 1:
    print(circle(float(input())))
elif choice == 2:
    print(rect(float(input()), float(input())))
else:
    print(triangle(float(input()), float(input())))

# Вариант 2
def hexagon(a):
    return 6 * (math.sqrt(3) / 4 * a * a)
print(hexagon(float(input())))

# Вариант 3
def hyp(a, b):
    return math.sqrt(a * a + b * b)
a1, b1 = float(input()), float(input())
a2, b2 = float(input()), float(input())
h1 = hyp(a1, b1)
h2 = hyp(a2, b2)
print("первая больше" if h1 > h2 else "вторая больше" if h2 > h1 else "равны")

# Вариант 4
def gcd(a, b):
    while b: a, b = b, a % b
    return a
A, B, C, D = int(input()), int(input()), int(input()), int(input())
num = A * D
den = B * C
g = gcd(num, den)
print(f"{num // g}/{den // g}")

# Вариант 5
def gcd(a, b):
    while b: a, b = b, a % b
    return a
A, B, C, D = int(input()), int(input()), int(input()), int(input())
num = A * D - C * B
den = B * D
g = gcd(abs(num), den)
print(f"{num // g}/{den // g}")

# Вариант 6
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def lcm(a, b): return a * b // gcd(a, b)
a, b = int(input()), int(input())
print(gcd(a, b))
print(lcm(a, b))

# Вариант 7
def area4(x, y, z, t):
    d = math.sqrt(x * x + y * y)
    p1 = (x + y + d) / 2
    p2 = (z + t + d) / 2
    return math.sqrt(p1 * (p1 - x) * (p1 - y) * (p1 - d)) + math.sqrt(p2 * (p2 - z) * (p2 - t) * (p2 - d))
x, y, z, t = float(input()), float(input()), float(input()), float(input())
print(area4(x, y, z, t))

# Вариант 8
def check(n):
    t = n
    while t:
        d = t % 10
        if d == 0 or n % d != 0:
            return False
        t //= 10
    return True
n = int(input())
for i in range(1, n + 1):
    if check(i):
        print(i)

# Вариант 9
def sum_digits(n):
    return sum(int(d) for d in str(n))
n = int(input())
cnt = 0
while n > 0:
    n -= sum_digits(n)
    cnt += 1
print(cnt)

# Вариант 10
def check_num(num, a, b, c):
    return all(ch in (str(a), str(b), str(c)) for ch in str(num))
N, a, b, c = int(input()), int(input()), int(input()), int(input())
cnt = 0
for i in range(100, N + 1):
    if check_num(i, a, b, c):
        cnt += 1
print(cnt)

# Вариант 11
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
n = int(input())
for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)

# Вариант 12
def div_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)
N = int(input())
for a in range(1, N + 1):
    b = div_sum(a)
    if b > a and div_sum(b) == a:
        print(a, b)

# Вариант 13
def is_armstrong(n):
    digs = [int(d) for d in str(n)]
    p = len(digs)
    return sum(d ** p for d in digs) == n
k = int(input())
for i in range(1, k + 1):
    if is_armstrong(i):
        print(i)

# Вариант 14
def div_count(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    return cnt
M, N = int(input()), int(input())
max_cnt = 0
res = []
for num in range(M, N + 1):
    cnt = div_count(num)
    if cnt > max_cnt:
        max_cnt = cnt
        res = [num]
    elif cnt == max_cnt:
        res.append(num)
print(*res)

# Вариант 15
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def bin_pal(n):
    b = bin(n)[2:]
    return b == b[::-1]
n = int(input())
for i in range(2, n + 1):
    if is_prime(i) and bin_pal(i):
        print(i)