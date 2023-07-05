import numpy

arr = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
print(numpy.max(numpy.min(arr, axis=1)))