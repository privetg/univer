# Вариант 1
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
s = cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i][j] > 0:
            s += A[i][j]
            cnt += 1
print(s)
print(cnt)

# Вариант 2
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
t = sum(m[0])
ok = True
for row in m:
    if sum(row) != t: ok = False
for j in range(n):
    if sum(m[i][j] for i in range(n)) != t: ok = False
if sum(m[i][i] for i in range(n)) != t: ok = False
if sum(m[i][n-1-i] for i in range(n)) != t: ok = False
print("магический" if ok else "не магический")

# Вариант 3
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
sym = all(m[i][j] == m[j][i] for i in range(n) for j in range(n))
print("симметричная" if sym else "не симметричная")

# Вариант 4
n, m = int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
sums = [sum(row) for row in mat]
max_i = sums.index(max(sums))
min_i = sums.index(min(sums))
print(*mat[max_i])
print(sums[max_i])
print(*mat[min_i])
print(sums[min_i])

# Вариант 5
n, m = int(input()), int(input())
mat = [sorted(list(map(int, input().split()))) for _ in range(n)]
for row in mat:
    print(*row)

# Вариант 6
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(max(mat[i]))
for j in range(n):
    print(min(mat[i][j] for i in range(n)))

# Вариант 7
n = int(input())
mat = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        v = int(input())
        mat[i][j] = mat[j][i] = v
for row in mat:
    print(*row)

# Вариант 8
n = int(input())
k = int(input())
mat = [list(map(float, input().split())) for _ in range(n)]
d = mat[k][k]
for j in range(n):
    mat[k][j] /= d
for row in mat:
    print(*row)

# Вариант 9
n = int(input())
k = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
multiples = [mat[i][j] for i in range(n) for j in range(n) if mat[i][j] % k == 0]
print(len(multiples))
if multiples:
    print(max(multiples))

# Вариант 10
n, m = int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
res = -10**9
for row in mat:
    if all(row[i] <= row[i+1] for i in range(m-1)) or all(row[i] >= row[i+1] for i in range(m-1)):
        res = max(res, max(row))
print(res if res != -10**9 else "нет")

# Вариант 11
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
mn = min(min(row) for row in mat)
for i in range(n):
    if mn in mat[i]:
        print(sum(mat[i]))
        break

# Вариант 12
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
res = []
for k in range(n):
    if mat[k] == [mat[i][k] for i in range(n)]:
        res.append(k)
print(*res)

# Вариант 13
n, m = int(input()), int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
for i in range(0, n, 2):
    print(min(mat[i]))

# Вариант 14
n = int(input())
m = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
max_row = max(range(n), key=lambda i: mat[i][i])
mat[max_row], mat[m] = mat[m], mat[max_row]
for row in mat:
    print(*row)

# Вариант 15
n, m = int(input()), int(input())
c = int(input())
d = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
rows = []
for i in range(n):
    if c in mat[i]:
        rows.append(i)
        for j in range(m):
            mat[i][j] *= d
print(*rows)
for row in mat:
    print(*row)