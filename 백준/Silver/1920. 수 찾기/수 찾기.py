n = int(input())
a = list(map(int, input().split()))
dic = dict()

for num in a:
    if num not in dic:
        dic[num] = 1

m = int(input())
b = list(map(int, input().split()))

for num in b:
    if num in dic:
        print(1)
    else:
        print(0)