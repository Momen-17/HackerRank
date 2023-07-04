import numpy

N, M = map(int, input().split())
attrs = ['add', 'subtract', 'multiply', 'floor_divide', 'mod', 'power']

A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

[print(getattr(numpy, attr)(A, B)) for attr in attrs]