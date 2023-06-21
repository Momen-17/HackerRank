n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    entries = input().split()
    B = set(map(int, input().split()))
    
    if entries[0] == "update":
        A.update(B)
    elif entries[0] == "intersection_update":
        A.intersection_update(B)
    elif entries[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    if entries[0] == "difference_update":
        A.difference_update(B)

print(sum(A))