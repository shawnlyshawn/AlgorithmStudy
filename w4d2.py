import sys

ans = {0: {1}, 1: {2, 3}}
for i in range(99999):
    a = {}
    for j in ans[i]:
        if j<=50000:
            ans[i+1].add(j*2)
        if j<=33334:
            ans[i+1].add(j*3)
        if j<=99999:
            ans[i+1].add(j+1)

n = int(sys.stdin.readline())
print()