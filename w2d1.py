import sys

m = int(input())

cups = [1, 2, 3]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    index_x = cups.index(x)
    index_y = cups.index(y)

    buffer = cups[index_x]
    cups[index_x] = cups[index_y]
    cups[index_y] = buffer

print(cups[0])