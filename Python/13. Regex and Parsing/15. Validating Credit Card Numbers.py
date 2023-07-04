import re

for _ in range(int(input())):
    match = re.match(r'^(?!.*(\d)(?:-?\1){3})[456]\d{3}(?:-?\d{4}){3}$', input())
    print('Valid' if match else 'Invalid')