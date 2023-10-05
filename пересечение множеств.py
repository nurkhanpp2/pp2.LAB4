a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
c = a & b
d = list(c)
d.sort()
print(*d)