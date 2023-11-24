n = int(input())

d = [0 for _ in range(n + 1)]
graph = [0]
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    x = i - 1
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        x = i // 3
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        x = i // 2

    graph.append(x)

result = [n]
while len(graph) > 1:
    x = graph[-1]
    result.append(x)
    graph = graph[:x]

print(d[n])
print(*result)
