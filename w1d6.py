import sys

n, m = map(int, sys.stdin.readline().split())

rec = [sys.stdin.readline().strip() for _ in range(n)]
max_len = min(n, m)

flag = 0
for i in range(max_len, 0, -1):
    if flag == 0 and i == 1:
        print(1)
        break
    for j in range(0, n-i+1):
        for k in range(0, m-i+1):

            if rec[j][k] == rec[j+i-1][k] == rec[j+i-1][k+i-1] == rec[j][k+i-1]:
                flag = 1
                print(i**2)
                break
            
        if flag:
            break
    if flag:
        break