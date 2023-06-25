from collections import Counter

s = input()
logo = Counter(list(sorted(s)))

print('\n'.join(char + ' ' + str(count) for char, count in logo.most_common(n=3)))