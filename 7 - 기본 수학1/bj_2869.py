# 달팽이는 올라가고 싶다

import sys, math

a, b, v = map(int, sys.stdin.readline().split())
v = (v - b) / (a - b)
    
print(math.ceil(v))
