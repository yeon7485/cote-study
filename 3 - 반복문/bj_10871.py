# X보다 작은 수

n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = list()
for i in l:
    if i < x:
        ans.append(i)
        
print(*ans)
