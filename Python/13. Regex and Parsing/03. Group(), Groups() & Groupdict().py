import re

matches = re.findall(r'([a-zA-Z0-9])\1', input())

print(matches[0] if matches else '-1')
