# Answer the boss - SPOJ
import queue

def topologicalSort(graph):
    indegree = [0] * V
    result = [0] * V
    zero_indegree = queue.Queue()
    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)
            result[i] += 1
    while not zero_indegree.empty():
        u = zero_indegree.get()
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)
                result[v] = result[u] + 1
    return  result


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        V, E = map(int, input().split())
        graph = [[] for i in range(V)]
        for j in range(E):
            u, v = map(int, input().split())
            graph[v].append(u)
        res = sorted(enumerate(topologicalSort(graph)), key=lambda tup: tup[1])
        print("Scenario #{0}:".format(i+1))
        for e in res:
            print(e[1], e[0])