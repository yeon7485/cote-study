#  다이얼

list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
time = 0
for i in range(len(word)):
    for j in range(len(list)):
        if word[i] in list[j]:
            time += j + 3

print(time)
