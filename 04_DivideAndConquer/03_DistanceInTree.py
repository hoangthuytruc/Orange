import sys
sys.setrecursionlimit(1000000)


def recursion(graph, u, par):
    count = {0: 1}
    res = 0
    for v in graph[u]:
        if v != par:
            res_v, count_v = recursion(graph, v, u)
            res += res_v

            count_v[-1] = 0

            for key, value in count_v.items():
                res += value * count.get(k - 1 - key, 0)

            for key, value in count_v.items():
                count[key + 1] = count.get(key + 1, 0) + value
    return res, count


if __name__ == '__main__':
    n, k = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    print(recursion(graph, 0, -1)[0])