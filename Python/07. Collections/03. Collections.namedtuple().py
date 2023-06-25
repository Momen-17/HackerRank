from collections import namedtuple

N, Student = int(input()), namedtuple("Student", input())
print("{:.2f}".format(sum([int(Student._make(input().split()).MARKS) for _ in range(N)]) / N))