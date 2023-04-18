# 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988

word = input()
check = 1
for i in range(int(len(word)/2)):
    if word[i] != word[-(i+1)]:
        check = 0
        break

print(check)
