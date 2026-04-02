from collections import deque

N, M, start = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list =[]
queue = deque()

def dfs(node):
    # 방문했다고 표시 -> 방문한 노드를 모아놓는 리스트 활용
    visited_list.append(node)
    # 할 일 하기
    print(node, end = ' ')
    # 순회시키기
    for adj_node in sorted(graph[node]):
        if adj_node not in visited_list:
            dfs(adj_node)

def bfs(start):
    queue.append(start)  
    while queue:
        node = queue.popleft()
        visited_list.append(node)  # 방문했다고 표시
        print(node, end = ' ')                # 할 일 하기 (objective)
        for adj_node in sorted(graph[node]):
            if adj_node not in visited_list:
                # print('>>>>', adj_node)
                if adj_node not in queue:
                    queue.append(adj_node)

dfs(start)
print()
visited_list.clear()
bfs(start)