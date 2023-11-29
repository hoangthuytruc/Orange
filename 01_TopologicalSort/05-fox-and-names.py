# Fox and Names - Codeforces
import sys
import queue

def getAscii(a):
    return ord(a) - ord('a')


def topologicalSort(graph, result):
    indegree = [0] * V
    zero_indegree = queue.Queue()

    for u in range(V):
        for v in graph[u]:
            indegree[v] += 1
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)
    for i in range(V):
        if indegree[i] != 0:
            return False
    return True


if __name__ == '__main__':
    V = 26
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    graph = [[] for _ in range(V)]
    result = []
    for i in range(0, len(names) - 1):
        isSuffix = True
        a = names[i]
        b = names[i+1]
        for j in range(len(a) if len(a) < len(b) else len(b)):
            if a[j] != b[j]:
                graph[getAscii(a[j])].append(getAscii(b[j]))
                isSuffix = False
                break
        if len(a) > len(b) and isSuffix:
            print("Impossible")
            exit()
    if topologicalSort(graph, result):
        for i in result:
            print(chr(i+97), end="")
    else:
        print("Impossible")