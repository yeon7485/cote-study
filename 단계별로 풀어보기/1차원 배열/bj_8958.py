# OX퀴즈

num = int(input())

for n in range(num):
    str = list(input())
    score = 0
    count = 1
    for i in str:
        if i == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)
