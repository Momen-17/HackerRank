N, M = map(int, input().split())

athletes_lists = []
for _ in range(N):
    attributes = list(map(int, input().split()))
    athletes_lists.append(attributes)

element = int(input())
for athlete in sorted(athletes_lists, key=lambda x: x[element]):
    print(*athlete)