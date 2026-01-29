# 1
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

# 2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# 3
a = int(input())
b = int(input())
for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)

# 4
n = int(input())
s = 0
for _ in range(n):
    s += int(input())
print(s)

# 5
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i ** 3
print(s)

# 6
n = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
print(f)

# 7
n = int(input())
s = 0
f = 1
for i in range(1, n + 1):
    f *= i
    s += f
print(s)

# 8
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# 9
n = int(input())
a, b = 0, 1
s = 0
for _ in range(n):
    s += a
    a, b = b, a + b
print(s)

# 10
n = int(input())
k = int(input())
a, b = 0, 1
count = 0
s = 0
while count < n + k - 1:
    if count >= k - 1:
        s += a
    a, b = b, a + b
    count += 1
print(s)