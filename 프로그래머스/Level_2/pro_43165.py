# lv.2 - 타겟 넘버
def solution(numbers, target):
    answer = 0

    def dfs(i, sum):
        nonlocal answer
        if i == len(numbers):
            if sum == target:
                answer += 1
            return
        dfs(i+1, sum + numbers[i])
        dfs(i+1, sum - numbers[i])
    
    dfs(0, 0)
    return answer
    
n = list(map(int, input().split()))
t = int(input())

print(solution(n, t))