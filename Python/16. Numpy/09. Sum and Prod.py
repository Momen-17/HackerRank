import numpy

arr = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
print(numpy.prod(numpy.sum(arr, axis=0)))