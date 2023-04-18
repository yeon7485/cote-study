# 문자열 반복

t = int(input())
for i in range(t):
    word = list(input().split())
    result = ""
    r = int(word[0])
    for j in range(len(word[1])):
        result += word[1][j] * r
    print(result)
