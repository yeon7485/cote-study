# A+B - 3

count = int(input())
l = list()
while count > 0:
    a, b = map(int, input().split())
    l.append(a + b)
    count -= 1

for n in l:
    print(n)