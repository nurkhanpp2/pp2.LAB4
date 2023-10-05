a = set(map(int,input().split()))
b = set(map(int,input().split()))
c = b & a
print(len(c))