import re

[print('YES' if re.search(r'^(7|8|9)[0-9]{9}$', input()) else 'NO') for _ in range(int(input()))]