
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

x, y = map(int, input().split())
day = y

for i in range(x - 1):
    day += date[i]

print(DAY[day % 7])
