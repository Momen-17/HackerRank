n, A = int(input()), set(map(int, input().split()))
l, B = int(input()), set(map(int, input().split()))

print(len(A.symmetric_difference(B)))