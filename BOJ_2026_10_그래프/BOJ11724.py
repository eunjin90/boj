import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
connected = 0

def dfs(node):
    visited[node] = True
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)

for node in range(1, N + 1):
    if not visited[node]:
        dfs(node)
        connected += 1

print(connected)