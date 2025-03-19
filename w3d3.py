import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)

def make_graph(i, j, compare):
    if (m*i+j) not in graph[compare]:
                    graph[compare].append(m*i+j)
                    graph[m*i+j].append(compare)

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage_field = {i: [0 for _ in range(m)] for i in range(n)}
    visited = {i: False for i in range(n*m)}

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage_field[y][x] = 1

    graph = {i: [] for i in range(m*n)}
    for i in range(n):
        for j in range(m):
            if cabbage_field[i][j]:
                graph[m*i+j].append(m*i+j)
                if j != 0 and cabbage_field[i][j-1]:
                    make_graph(i, j-1, m*i+j)
                if j != m-1 and cabbage_field[i][j+1]:
                    make_graph(i, j+1, m*i+j)
                if i != 0 and cabbage_field[i-1][j]:
                    make_graph(i-1, j, m*i+j)
                if i != n-1 and cabbage_field[i+1][j]:
                    make_graph(i+1, j, m*i+j)

    for i in range(n*m):
        if len(graph[i]) == 0:
            graph.pop(i)
            visited.pop(i)
        else:
            if len(graph[i]) == 1 and graph[i] == [i]:
                graph[i] = []
            if i in graph[i]:
                graph[i].remove(i)

    connected = 0
    for i in range(n*m):
        if i in visited.keys():
            if not visited[i]:
                dfs(graph, i, visited)
                connected += 1
                
    print(connected)