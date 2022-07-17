# 그룹 단어 체커

n = int(input())
count = n
for i in range(n):
    word = input()
    s = [word[0]]
    for j in range(1, len(word) - 1):
        if word[j] != word[j+1] and word[j+1] in s:
            count -= 1
            break

        if word[j] in s:
            continue
        else:
            s.append(word[j])

print(count)

