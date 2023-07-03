import re

css_block = ''
valid_colors = []
for _ in range(int(input())):
    css_block += input()

valid_colors = re.findall(r'{([^{}]+)}', css_block)
print(*re.findall(r'#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}', str(valid_colors)), sep='\n')
