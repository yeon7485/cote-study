# 알파벳 찾기

word = input()
result = []
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in word:
        result.append(word.find(chr(i)))
    else:
        result.append(-1)

print(*result)