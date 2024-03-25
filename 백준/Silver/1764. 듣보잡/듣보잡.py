n, m = list(map(int, input().split()))
set1 = set(input() for _ in range(n))
set2 = set(input() for _ in range(m))

rst = sorted(list(set1 & set2))
print(len(rst))
for r in rst:
    print(r)
