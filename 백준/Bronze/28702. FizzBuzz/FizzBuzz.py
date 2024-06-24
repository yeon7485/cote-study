a = input()
b = input()
c = input()
rst = 0
if a.isdigit():
    rst = int(a) + 3
elif b.isdigit():
    rst = int(b) + 2
elif c.isdigit():
    rst = int(c) + 1

if rst % 3 == 0 and rst % 5 == 0:
    print('FizzBuzz')
elif rst % 3 == 0 and rst % 5 != 0:
    print('Fizz')
elif rst % 3 != 0 and rst % 5 == 0:
    print('Buzz')
else:
    print(rst)