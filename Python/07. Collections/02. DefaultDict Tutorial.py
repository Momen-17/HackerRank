from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)

for index in range(n):
    A[input()].append(index + 1)

for _ in range(m):
    print(*A.get(input(), [-1]))