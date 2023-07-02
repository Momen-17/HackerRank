P, K = map(int, input().split())
x = P
equation = input()
print('True' if eval(equation) == K else 'False')