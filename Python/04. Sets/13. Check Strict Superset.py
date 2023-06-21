A = set(map(int, input().split()))
print(all(A > set(map(int, input().split())) for _ in range(int(input()))))