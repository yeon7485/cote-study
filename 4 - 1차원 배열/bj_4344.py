# 평균은 넘겠지

c = int(input())

for i in range(c):
    score = list(map(int, input().split()))
    n = score[0]
    del score[0]
    
    count = 0
    avg = sum(score) / n
    for s in score:
        if avg < s:
            count += 1
    print("{:.3f}%".format(count / n * 100))
    