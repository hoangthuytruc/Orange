# Beverages - UVA
import heapq

def topologicalSort(graph, result):
    indegree = [0] * V
    zero_indegree = []
    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(V):
        if indegree[i] == 0:
            heapq.heappush(zero_indegree, i)
    while not len(zero_indegree) == 0:
        u = heapq.heappop(zero_indegree)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(zero_indegree, v)


if __name__ == '__main__':
    tc = 0
    while True:
        try:
            tc += 1
            V = int(input())
            beverages = {}
            graph = [[] for i in range(V)]
            result = []
            for i in range(V):
                beverages[input()] = i
            E = int(input())
            for i in range(E):
                u, v = input().split()
                graph[beverages[u]].append(beverages[v])
            topologicalSort(graph, result)
            beverages = {v: k for k, v in beverages.items()}
            beverages_order = []
            for v in result:
                beverages_order.append(beverages[v])
            print("Case #{0}: Dilbert should drink beverages in this order: {1}.".format(tc, ' '.join(map(str, beverages_order))))
            print()
            input()
        except EOFError:
            break
