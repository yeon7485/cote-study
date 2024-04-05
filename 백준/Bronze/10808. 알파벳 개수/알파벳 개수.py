s = input()
cnt = [0] * 26

for i in range(len(s)):
    cnt[ord(s[i]) - ord('a')] += 1
    
print(*cnt)