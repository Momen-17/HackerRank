import re

matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])', input())
print('\n'.join(matches) if matches else '-1')
