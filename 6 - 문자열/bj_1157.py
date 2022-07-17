# 단어 공부

word = input().upper()
arr = []
for i in range(ord('A'), ord('Z') + 1):
    arr.append(word.count(chr(i)))

max = max(arr)
result = chr(arr.index(max) + ord('A'))

for i in range(len(arr)):
    if arr[i] == max and i != arr.index(max):
        result = '?'

print(result)


# # 두 번째 방법

# word = input().upper()
# arr = list(set(word))
# count = []
# for a in arr:
#     count.append(word.count(a))

# max = max(count)
# if count.count(max) > 1:
#     print('?')
# else:
#     print(arr[count.index(max)])