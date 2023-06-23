from itertools import groupby

print(*[(len(list(X)), int(c)) for c, X in groupby(input)])
