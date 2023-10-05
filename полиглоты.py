lang = []
union = set()
all = set()
for i in range(int(input())):
    a = int(input())
    b = {input() for j in range(a)}
    all.update(b)
    if i == 1:
        union.update(b)
    else:
        union &= b
print(len(union))
print('\n'.join(sorted(union)))
print(len(all))
print('\n'.join(sorted(all)))