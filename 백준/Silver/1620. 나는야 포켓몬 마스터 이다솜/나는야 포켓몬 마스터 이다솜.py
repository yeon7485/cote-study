import sys

n, m = map(int, sys.stdin.readline().split())

pokemon = {}

for i in range(1, n+1):
    p = sys.stdin.readline().rstrip()
    pokemon[i] = p
    pokemon[p] = i

for i in range(m):
    find = sys.stdin.readline().rstrip()
    if find.isdigit():
        print(pokemon[int(find)])
    else:
        print(pokemon[find])
