import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
