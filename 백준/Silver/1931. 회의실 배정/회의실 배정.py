N = int(input())
meet = []
for _ in range(N):
    s, f = list(map(int, input().split()))
    meet.append([f, s])
meet.sort()
finish = 0
result = 0
for m in meet:
    if finish <= m[1]:
        finish = m[0]
        result += 1

print(result)
