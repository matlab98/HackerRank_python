import numpy

n, m = map(int, raw_input().split(" "))
array = numpy.array([raw_input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

#python 2

import numpy
N, M = map(int, raw_input().split())
s = numpy.array([map(int, raw_input().split()) for _ in range(N)])
print(numpy.transpose(s))
print(s.flatten())