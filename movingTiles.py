__author__ = 'Robert'

import math

l, s1, s2 = input().split()
l, s1, s2 = float(l),float(s1), float(s2)

x1 = math.sqrt((s1*s1)/2.0)
x2 = math.sqrt((s2*s2)/2.0)

t = int(input())
for ii in range(t):
    a = float(input())

    z = (math.sqrt(a) - l)/ (x1 - x2)

    print(abs(z))

