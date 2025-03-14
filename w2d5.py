import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())

n_list = []
s = []
for i in range(n):
    n_list.append(i)
    s.append(list(map(int, sys.stdin.readline().split())))

combi = list(combinations(n_list, int(n/2)))
combi = combi[0:int(len(combi)/2)]

ans = float('inf')

for c in combi:
    start = list(c)
    link = list(set(n_list) - set(start))
    
    start_sum = 0
    link_sum = 0
    
    for i, j in combinations(start, 2):
        start_sum += s[i][j] + s[j][i]
    
    for i, j in combinations(link, 2):
        link_sum += s[i][j] + s[j][i]
    
    ans = min(ans, abs(start_sum - link_sum))

print(ans)