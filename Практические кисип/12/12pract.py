# Блок А: задача 4
def sum_digits(n):
    return n % 10 + sum_digits(n // 10) if n else 0

n = int(input())
print(sum_digits(n))

# Блок Б: задача 1
def find_max():
    x = int(input())
    if x == 0:
        return x
    return max(x, find_max())

print(find_max())