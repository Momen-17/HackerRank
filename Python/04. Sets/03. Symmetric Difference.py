n = int(input())
A = set(map(int, input().split()))
l = int(input())
B = set(map(int, input().split()))

print(*sorted(A.symmetric_difference(B)), sep="\n")