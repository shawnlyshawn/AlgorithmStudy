import sys

n = int(sys.stdin.readline().rstrip())

t_list = []
p_list = []
dp = []
for i in range(n+1):
    if i != n:
        t, p = map(int, sys.stdin.readline().split())
        t_list.append(t)
        p_list.append(p)
    dp.append(0)    

for i in range(n-1, -1, -1):
    if t_list[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[t_list[i]+i]+p_list[i])

print(dp[0])