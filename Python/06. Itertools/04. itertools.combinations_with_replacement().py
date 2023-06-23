from itertools import combinations_with_replacement

string = input().split()
S, k = sorted(string[0]), int(string[1])

for item in combinations_with_replacement(S, k):
    print(''.join(item))