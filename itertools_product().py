# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a1, a2 = map(int, input().split(" "))
b1, b2 = map(int, input().split(" "))
A = [a1, a2]
B = [b1, b2]
x = lst = list(x for x in product(A,B))

for i in x:
    print(i, end = ' ' )

# A better version of the above code is:

import itertools as it
a = list(map(int , input("").split(' ')))
b = list(map(int , input("").split(' ')))
lst = list(x for x in it.product(a,b))
for i in lst:
    print(i, end = ' ' )