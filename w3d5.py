import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

MAX = 100001
visited = [0] * MAX

q = deque()
q.append(n)

while q:
    cur = q.popleft()
    
    if cur == k:
        print(visited[cur])
        break

    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next < MAX and visited[next] == 0:
            visited[next] = visited[cur] + 1
            q.append(next)