import heapq

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    graph: dict {u: [(v, weight), ...]}
    """
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)] # (distance, vertex)
    visited = [False] * n

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
                
    return dist, prev

def reconstruct_path(prev, source, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    if path and path[0] == source:
        return path
    return []

# Graph Definition (Adjacency List)
# 0-indexed nodes: 0, 1, 2, 3, 4, 5
graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 1), (3, 7)],
    2: [(4, 3)],
    3: [(5, 1)],
    4: [(3, 2), (5, 5)],
    5: []
}

source = 0
dist, prev = dijkstra(graph, source)

print(f"Shortest paths from vertex {source}:")
print(f"{'Target':<10} {'Distance':<10} {'Path':<20}")
for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = " -> ".join(map(str, path)) if path else "No Path"
    d_val = dist[v] if dist[v] != float('inf') else "INF"
    print(f"{v:<10} {d_val:<10} {path_str:<20}")
