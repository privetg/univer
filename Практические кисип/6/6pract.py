# Вариант 0
n = int(input())
m = int(input())
x = [int(input()) for _ in range(n)]
y = [i for i in x if abs(i) > m]
print(m)
print(x)
print(y)

# Вариант 1
n = int(input())
arr = [int(input()) for _ in range(n)]
print(max(arr))

# Вариант 2
n = int(input())
arr = [int(input()) for _ in range(n)]
print(min(arr))
print(arr.index(min(arr)))

# Вариант 3
n = int(input())
D = [int(input()) for _ in range(n)]
s = sum(D[i] for i in range(1, n, 2))
print(D)
print(s)

# Вариант 4
arr = [int(input()) for _ in range(8)]
print(max(arr))
print(arr.index(max(arr)))

# Вариант 5
arr = [int(input()) for _ in range(10)]
for i in range(9):
    if arr[i] < 0 and arr[i + 1] < 0:
        print(arr[i], arr[i + 1])

# Вариант 6
arr = [int(input()) for _ in range(10)]
m = max(arr)
less = sum(1 for x in arr if x < m)
greater = sum(1 for x in arr if x > m)
print(less)
print(greater)

# Вариант 7
n = int(input())
arr = [int(input()) for _ in range(n)]
even_sum = sum(arr[i] for i in range(0, n, 2))
odd_prod = 1
for i in range(1, n, 2):
    odd_prod *= arr[i]
print(even_sum)
print(odd_prod)

# Вариант 8
arr = [int(input()) for _ in range(8)]
print(sum(arr))
prod = 1
for x in arr:
    prod *= x
print(prod)

# Вариант 9
arr = [int(input()) for _ in range(10)]
print(min(abs(x) for x in arr))
print(arr[::-1])

# Вариант 10
arr = [int(input()) for _ in range(8)]
seen = set()
dups = []
for x in arr:
    if x in seen and x not in dups:
        dups.append(x)
    seen.add(x)
print(dups if dups else "нет")

# Вариант 11
arr = [int(input()) for _ in range(10)]
even = [x for x in arr if x % 2 == 0]
print(max(even) if even else "нет")

# Вариант 12
arr = [int(input()) for _ in range(10)]
odd = [x for x in arr if x % 2 != 0]
print(min(odd) if odd else "нет")

# Вариант 13
arr = [int(input()) for _ in range(8)]
d = {}
for i, x in enumerate(arr):
    if x in d:
        d[x].append(i)
    else:
        d[x] = [i]
for k, v in d.items():
    if len(v) > 1:
        print(k, v)

# Вариант 14
arr = [int(input()) for _ in range(10)]
mi = arr.index(min(arr))
ma = arr.index(max(arr))
arr[mi], arr[ma] = arr[ma], arr[mi]
print(arr)

# Вариант 15
arr = [int(input()) for _ in range(10)]
seen = set()
dups = []
for x in arr:
    if x in seen and x not in dups:
        dups.append(x)
    seen.add(x)
print(dups)