import re

matrix = []
for _ in range(int(input().split()[0])):
    matrix.append(input())

decoded = ''.join(list(map(''.join, zip(*matrix))))
print(re.sub(r'\b\W+\b', ' ', decoded))
