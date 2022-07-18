# 분수찾기

import sys

n = int(sys.stdin.readline())
line = 0
end = 0

while n > end:
    line += 1
    end += line

if line % 2 == 0:
    top = line - (end - n)
    bottom = end - n + 1
else:
    top = end - n + 1
    bottom = line - (end - n)

print(f"{top}/{bottom}")
