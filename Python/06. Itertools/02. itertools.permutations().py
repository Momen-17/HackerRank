from itertools import permutations

S, k = input().split()

for item in sorted(list(permutations(S, int(k)))):
    print(''.join(item))