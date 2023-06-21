N = int(input())

for _ in range(N):
    a, A = int(input()), set(map(int, input().split()))
    b, B = int(input()), set(map(int, input().split()))
    
    print(A.issubset(B))