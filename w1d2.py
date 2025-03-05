lst = []
height_sum = 0

for i in range(0, 9):
    height = int(input())
    lst.append(height)
    height_sum += height

lst.sort()

find_sum = height_sum - 100

for height in lst:
    if (find_sum - height) in lst:
        lst.remove(height)
        lst.remove((find_sum - height))
        break

for ans in lst:
    print(ans)