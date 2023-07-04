regex_integer_in_range = r'^(?!000000)\d{6}$'
regex_alternating_repetitive_digit_pair = r'(?=(\d)\d\1)'


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)