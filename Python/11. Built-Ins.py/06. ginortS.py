S = input()
sorted_S = sorted(S, key= lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower()))
print(*sorted_S, sep='')
