# Вариант 1
text = input()
words = text.split()
count = sum(1 for w in words if w[0].lower() == 'е')
print(count)

# Вариант 2
text = input()
new = text.replace(':', '%')
print(new)
print(text.count(':'))

# Вариант 3
text = input()
new = text.replace('.', '')
print(new)
print(text.count('.'))

# Вариант 4
text = input()
new = text.replace('а', 'о').replace('А', 'О')
print(new)
print(text.count('а') + text.count('А'))
print(len(text))

# Вариант 5
text = input()
print(text.lower())

# Вариант 6
text = input()
new = text.replace('а', '').replace('А', '')
print(new)
print(text.count('а') + text.count('А'))

# Вариант 7
text = input()
n = len(text)
res = list(text)
for i in range(n // 2):
    if res[i].lower() == 'п':
        res[i] = '*'
print(''.join(res))

# Вариант 8
text = input()
words = text.rstrip('.').split()
print(len(words))

# Вариант 9
text = input()
word = input()
print(text.lower().split().count(word.lower()))

# Вариант 10
text = input()
print(' '.join(w.capitalize() for w in text.split()))

# Вариант 11
text = input()
max_len = 0
curr = 0
for ch in text:
    if ch == 'н':
        curr += 1
        max_len = max(max_len, curr)
    else:
        curr = 0
new = text.replace('!', '.')
print(max_len)
print(new)

# Вариант 12
text = input()
for w in text.split():
    if w.endswith('я'):
        print(w)

# Вариант 13
text = input()
start = text.find('(')
end = text.find(')')
if start != -1 and end != -1:
    print(text[start + 1:end])

# Вариант 14
text = input()
for w in text.split():
    if w[0].lower() == 'а':
        print(w)
for w in text.split():
    if w[-1].lower() == 'я':
        print(w)

# Вариант 15
text = input()
print(text.lower().count('т'))