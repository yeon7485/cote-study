# 크로아티아 알파벳

list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
count = 0
for l in list:
    if l in word:
        count += word.count(l)
        word = word.replace(l, "0")
count += len(word) - word.count("0")
print(count)