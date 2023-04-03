# 평균

n = int(input())
score = list(map(int, input().split()))

ans = 0
for s in score:
    ans += s / max(score) * 100
    
print(ans/n)