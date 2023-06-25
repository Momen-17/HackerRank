from collections import Counter

money = 0
X = int(input())
sizes = Counter(map(int, input().split()))
N = int(input())

for _ in range(N):
    size, price = map(int, input().split())
    if sizes[size]:
        money += price
        sizes[size] -= 1

print(money)