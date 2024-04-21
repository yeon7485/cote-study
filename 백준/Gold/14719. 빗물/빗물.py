H, W = map(int, input().split())
height = list(map(int, input().split()))
ans = 0

for i in range(1, W - 1):
    # 인덱스 기준 왼쪽/오른쪽에서 제일 높은 블록 구하기
    max_left = max(height[:i])
    max_right = max(height[i:])

    # 빗물이 쌓일 수 있는 높이
    rain_height = min(max_left, max_right)
    # 고이는 빗물 더해주기
    if rain_height > height[i]:
        ans += rain_height - height[i]

print(ans)
