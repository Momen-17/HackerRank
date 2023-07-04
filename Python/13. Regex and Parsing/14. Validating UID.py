import re

for _ in range(int(input())):
    match = re.match(r'^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z0-9]{10}$', input())
    print('Valid' if match else 'Invalid') 