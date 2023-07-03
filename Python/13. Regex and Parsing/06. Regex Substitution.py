import re

lines = []
for _ in range(int(input())):
    lines.append(input())

replacement = {"&&": "and", "||": "or"}
[print(re.sub(r"(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)", lambda m: replacement[m.group(0)], line)) for line in lines]
