import re

S, k = input(), input()
[print((match.start(), match.start() + len(k) - 1)) for match in re.finditer(f'(?={k})', S)]
if not re.search(f'(?={k})', S):
    print((-1, -1))
