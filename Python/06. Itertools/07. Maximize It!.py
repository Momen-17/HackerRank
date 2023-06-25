from itertools import product

K, M = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(K))
print(max(sum(i**2 for i in lst) % M for lst in product(*n)))