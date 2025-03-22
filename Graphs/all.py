# Adjacency List

from collections import defaultdict

graph = defaultdict(list)

def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

# print(dict(graph))

# Graph traversal Algorithms 

# DFS - Recursive

def dfs_recursive(node, visited, graph):
    if node in visited: 
        return
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        dfs_recursive(neighbor, visited, graph)

visited = set()
# dfs_recursive(0, visited, graph)

# BFS - using Queue

from collections import deque

def bfs(start, graph):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
# bfs(0, graph)

# Detect Cycle in undirected Graph (DFS)

def has_cycle(node, parent, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(neighbor, node, visited, graph):
                return True
        elif neighbor !=parent:
            return True
    return False
visited = set()
cycle = False
for node in graph:
     if node not in visited:
         if has_cycle(node, -1, visited, graph):
             cycle = True
             break
print("Cycle:", cycle)
