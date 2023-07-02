P, K = map(int, input().split())
x, equation = P, input()
print('True' if eval(equation) == K else 'False')