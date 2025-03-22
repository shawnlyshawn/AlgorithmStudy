import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
cnt = [0] * MAX

q = deque()
q.append(n)

visited[n] = 0
cnt[n] = 1

while q:
    cur = q.popleft()

    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next < MAX:
            if visited[next] == -1:
                visited[next] = visited[cur] + 1
                cnt[next] = cnt[cur]
                q.append(next)
            elif visited[next] == visited[cur] + 1:
                cnt[next] += cnt[cur]

print(visited[k])
print(cnt[k])