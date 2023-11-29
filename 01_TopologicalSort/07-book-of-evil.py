# Book of Evil - Codeforces
import sys
sys.setrecursionlimit(1000000)
INF = 1000000000


def DFS(graph, dist, affected, u, d):
    dist[u] = -INF
    if affected[u]:
        dist[u] = d

    for v in graph[u]:
        if dist[v] == -1:
            DFS(graph, dist, affected, v, d + 1)


if __name__ == '__main__':
    n, m, d = map(int, input().split())

    p_list = list(map(int, input().split()))
    affected = [False] * (n+1)
    for i in p_list:
        affected[i] = True

    graph = [[] for _ in range(n + 1)]
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist0 = [-1] * (n + 1)
    DFS(graph, dist0, affected, 1, 0)
    u = dist0.index(max(dist0))

    u_dist = [-1] * (n + 1)
    DFS(graph, u_dist, affected, u, 0)
    v = u_dist.index(max(u_dist))

    affected = [True] * (n + 1)
    u_dist = [-1] * (n + 1)
    DFS(graph, u_dist, affected, u, 0)
    v_dist = [-1] * (n + 1)
    DFS(graph, v_dist, affected, v, 0)

    res = 0
    for i in range(1, n + 1):
        if max(u_dist[i], v_dist[i]) <= d:
            res += 1
    print(res)
