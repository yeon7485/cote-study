def recursion(s, l, r, count):
    if l >= r:
        return (1, count)
    elif s[l] != s[r]:
        return (0, count)
    else :
        count += 1
        return recursion(s, l+1, r-1, count)

t = int(input())
for i in range(t):
    word = input()
    
    print(*recursion(word, 0, len(word)-1, 1))