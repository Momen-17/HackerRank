from itertools import product

A = map(int, input().split())
B = map(int, input().split())

[print(group, end=" ") for group in list(product(A, B))]