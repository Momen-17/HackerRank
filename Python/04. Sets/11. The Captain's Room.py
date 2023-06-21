K = int(input())
rooms = list(map(int, input().split()))
print((sum(set(rooms)) * K - sum(rooms)) // (K - 1))