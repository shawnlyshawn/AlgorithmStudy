import sys
from collections import deque

def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def bfs(start):
    visited = {i: False for i in graph}
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

visited_dfs = {i: False for i in graph}
dfs(v, visited_dfs)
print()
bfs(v)