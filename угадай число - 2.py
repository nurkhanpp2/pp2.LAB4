x = int(input())
a = set(range(1, x + 1))
b = a
while True:
    c = input()
    if c == 'HELP':
        break
    c = {int(i) for i in c.split()}
    if len(b & c) > len(b) / 2:
        print('YES')
        b &= c
    else:
        print('NO')
        b &= a - c
         
print(' '.join([str(i) for i in sorted(b)]))