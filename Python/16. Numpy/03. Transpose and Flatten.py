import numpy

arr = numpy.array([list(map(int, input().split())) for _ in range(int(input().split()[0]))])
print(numpy.transpose(arr))
print(arr.flatten())