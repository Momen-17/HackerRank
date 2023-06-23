from itertools import combinations

N, letters, K = int(input()), input().split(), int(input())

count = 0
for item in list(combinations(letters, K)):
    if 'a' in item:
        count += 1

print("{:.12f}".format(count / len(list(combinations(letters, K)))))