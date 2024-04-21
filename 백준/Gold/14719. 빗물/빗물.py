H, W = map(int, input().split())
height = list(map(int, input().split()))
ans = 0

for i in range(1, W - 1):
    max_left = max(height[:i])
    max_right = max(height[i:])
    rain = min(max_left, max_right)
    ans += max(0, rain - height[i])

print(ans)
