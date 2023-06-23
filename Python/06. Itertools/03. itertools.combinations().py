from itertools import combinations

string = input().split()
S, k = sorted(string[0]), int(string[1])

for i in range(1, k + 1):
    print(*list(map(''.join, combinations(S, i))), sep='\n')