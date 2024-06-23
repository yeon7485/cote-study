n = int(input())
arr = list(input())
rst = 0

for i in range(n):
    rst += ((ord(arr[i]) - 96) * (31 ** i))

print(rst % 1234567891)