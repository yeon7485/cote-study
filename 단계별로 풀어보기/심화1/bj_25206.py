# 너의 평점은
# https://www.acmicpc.net/problem/25206

g = {'A+': 4.5, 'A0':	4.0, 'B+': 3.5, 'B0': 3.0,
     'C+': 2.5, 'C0':	2.0, 'D+': 1.5, 'D0': 1.0, 'F':	0.0}

score = 0
grade = 0
for _ in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue
    score += float(b)
    grade += g[c] * float(b)

print(round(grade / score, 6))
