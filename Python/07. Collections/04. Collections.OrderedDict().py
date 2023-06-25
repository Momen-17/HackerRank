from collections import OrderedDict

sales = OrderedDict()

for _ in range(int(input())):
    name, price = input().rsplit(" ", 1)
    sales[name] = sales.get(name, 0) + int(price)

[print(name, price) for name, price in sales.items()]