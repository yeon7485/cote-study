# 소트인사이드

import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, str(n))), reverse=True)
print(*arr, sep="")