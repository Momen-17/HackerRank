import numpy

N = int(input())
A = numpy.array([list(map(int, input().split())) for _ in range(N)]) 
B = numpy.array([list(map(int, input().split())) for _ in range(N)]) 
numpy.set_printoptions(legacy='1.13')
print(numpy.dot(A, B))