import heapq


def topologicalSort(graph):
    indegree = [0] * (V+1)
    zero_indegree = []
    delta = len(graph) - 2
    ans = 0
    for u in range(1, V+1):
        for v in graph[u]:
            indegree[v] += 1

    for i in range(1, V+1):
        if indegree[i] == 0:
            heapq.heappush(zero_indegree, (minutes[i - 1], i))

    while not len(zero_indegree) == 0:
        u = heapq.heappop(zero_indegree)
        cost = u[0] + delta
        ans = max(ans, cost)
        delta -= 1
        for v in graph[u[1]]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(zero_indegree, (minutes[v - 1], v))
    return ans


if __name__ == '__main__':
    V = int(input())
    graph = [[] for _ in range(V + 1)]
    minutes = []
    for i in range(1, V + 1):
        line = list(map(int, input().split()))
        minutes.append(line[0])
        E = line[1]
        for j in line[2: len(line)]:
            graph[i].append(j)
    res = topologicalSort(graph)
    print(res)
