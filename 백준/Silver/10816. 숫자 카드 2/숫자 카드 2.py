import sys

N = int(input())
cards = {}
arr = list(map(int, sys.stdin.readline().split()))
ans = ''
for a in arr:
    if a in cards:
        cards[a] += 1
    else:
        cards[a] = 1

M = int(input())
cnt_cards = list(map(int, sys.stdin.readline().split()))
ans = [0] * M
for i in range(M):
    if cnt_cards[i] in cards:
        ans[i] += cards[cnt_cards[i]]

print(*ans)
