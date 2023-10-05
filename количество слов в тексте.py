count_of_str = int(input())
list = []
for i in range(count_of_str):
    for element in input().split():
        list.append(element)
print(len(set(list)))