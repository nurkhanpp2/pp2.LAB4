n = int(input())
ans = set(range(1, n + 1))
x = 0
while True:
    x = input()
    if x == "HELP":
        break
    else:
        a = set(list(map(int, x.split())))
        x = input()
        if x == "YES":
            ans = ans & a
        else:
            ans = ans - a
ans = sorted(ans)
print(*ans)