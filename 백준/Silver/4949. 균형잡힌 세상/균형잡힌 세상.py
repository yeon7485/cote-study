# 균형잡힌 세상

from collections import deque

while True:
    s = input()
    ans = 'yes'
    if s == '.':
        break
    stack = deque()

    for i in range(len(s)):
        if s[i] == '[' or s[i] == '(':
            stack.append(s[i])
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ans = 'no'
                break
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 'no'
                break

    if len(stack) > 0:
        ans = 'no'
    print(ans)
