# 카드 놓기

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
visited = [False] * n
answer = set()

def dfs(count, arr):
    if count == k:
        num = ""
        for j in range(k):
            num += arr[j]
        answer.add(num)
        return

    for i, card in enumerate(cards):
        if not visited[i]:
            arr.append(card)
            visited[i] = True
            dfs(count + 1, arr)
            arr.pop()
            visited[i] = False

dfs(0, [])
print(len(answer))