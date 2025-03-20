import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited, houses, complex_num):
    visited[v] = True
    houses[complex_num].append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, houses, complex_num)

def make_graph(i, j, compare):
    if compare not in graph:
        graph[compare] = []
    if (n*i+j) not in graph:
        graph[n*i+j] = []
    
    graph[compare].append(n*i+j)
    graph[n*i+j].append(compare)

n = int(sys.stdin.readline().strip())
map = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

visited = {i: False for i in range(n*n)}
graph = {i: [] for i in range(n*n)}

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            if j > 0 and map[i][j-1] == 1:
                make_graph(i, j-1, n*i+j)
            if j < n-1 and map[i][j+1] == 1:
                make_graph(i, j+1, n*i+j)
            if i > 0 and map[i-1][j] == 1:
                make_graph(i-1, j, n*i+j)
            if i < n-1 and map[i+1][j] == 1:
                make_graph(i+1, j, n*i+j)

complexes = 0
houses = {}

for i in range(n*n):
    if map[i//n][i%n] == 1 and not visited[i]:
        houses[complexes] = []
        dfs(graph, i, visited, houses, complexes)
        complexes += 1
print(complexes)

house_counts = sorted([len(houses[i]) for i in range(complexes)])
for count in house_counts:
    print(count)