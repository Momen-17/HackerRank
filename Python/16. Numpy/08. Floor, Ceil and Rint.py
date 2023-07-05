import numpy

numpy.set_printoptions(legacy='1.13')
arr, attrs = numpy.array(input().split(), float), ['floor', 'ceil', 'rint']
[exec(f'print(numpy.{attr}(arr))') for attr in attrs]