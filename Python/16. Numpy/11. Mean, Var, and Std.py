import numpy

arr = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
print(numpy.mean(arr, axis=1), numpy.var(arr, axis=0), round(numpy.std(arr), 11), sep='\n')