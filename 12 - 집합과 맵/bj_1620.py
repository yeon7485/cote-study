# 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())

pokemon = [0] * n

for i in range(n):
    pokemon[i] = sys.stdin.readline()

for i in range(m):
    find = sys.stdin.readline()
    if 49 <= ord(find[0]) and ord(find[0]) <= 57:
        print(pokemon[int(find) - 1])
    else:
        print(pokemon.index(find) + 1)
