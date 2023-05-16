# 예산


def solution(d, budget):
    answer = 0
    d.sort()

    for x in d:
        budget -= x
        if budget < 0:
            break
        else:
            answer += 1

    return answer


arr = list(map(int, input().split()))
budget = int(input())
print(solution(arr, budget))
