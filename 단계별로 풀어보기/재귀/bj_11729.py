# 하노이 탑 이동 순서

def hanoi(n, start, end):
    if n == 0:
        return

    other = 6 - start - end
    hanoi(n-1, start, other)
    print(start, end)
    hanoi(n-1, other, end)


n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)
