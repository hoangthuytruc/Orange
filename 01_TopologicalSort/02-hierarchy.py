# Hierarchy - SPOJ
import queue

def topologicalSort(graph, result):
    indegree = [0] * (V+1)
    zero_indegree = queue.Queue()
    for u in range(1, V+1):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(1, V+1):
        if indegree[i] == 0:
            zero_indegree.put(i)
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)


if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]
    result = []
    for i in range(E):
        v_list = list(map(int, input().split()))
        for v in v_list[1:]:
            graph[i+1].append(v)
    topologicalSort(graph, result)
    positions = [0] * (len(result) + 1)
    for idx in range(len(result)):
        if idx > 0:
            positions[result[idx]] = result[idx-1]
    for p in positions[1:]:
        print(p)


