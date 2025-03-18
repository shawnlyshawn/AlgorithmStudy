import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)

graph = {i: [] for i in range(1, n + 1)} 
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

connected = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        connected += 1

print(connected)