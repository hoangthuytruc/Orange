# Topological Sorting - SPOJ
import heapq

def topologicalSort(graph, result):
    indegree = [0] * (V+1)
    zero_indegree = []
    for u in range(1, V+1):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(1, V+1):
        if indegree[i] == 0:
            heapq.heappush(zero_indegree, i)
    while not len(zero_indegree) == 0:
        u = heapq.heappop(zero_indegree)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(zero_indegree, v)
    for i in range(1, V+1):
        if indegree[i] != 0:
            return False
    return True


if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]
    result = []
    for i in range(1, E+1):
        u, v = map(int, input().split())
        graph[u].append(v)
    if topologicalSort(graph, result):
        for i in range(V):
            print(result[i], end= ' ')
    else:
        print('Sandro fails.')


