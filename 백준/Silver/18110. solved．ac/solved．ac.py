# solved.ac
import sys


N = int(sys.stdin.readline())
if N == 0:
    print(0)
else:
    opi = [int(sys.stdin.readline()) for _ in range(N)]
    cut = int(N * 0.15 + 0.5)
    n = N - cut * 2

    opi.sort()
    average = int(sum(opi[cut:(N - cut)]) / n + 0.5)
    print(average)
