# 단어 정렬

import sys

n = int(sys.stdin.readline())
word = set()

for _ in range(n):
    word.add(sys.stdin.readline().strip())

word = list(word)
word.sort()
word.sort(key=len)

for w in word:
    print(w)