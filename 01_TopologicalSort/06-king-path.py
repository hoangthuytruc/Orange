# King's Path - Codeforces
import queue
MAX = 10**9
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
graph = set()
dist = {}


def convertToNumber(x, y):
    global MAX
    return x * MAX + y


def BFS(x0, y0, x1, y1):
    global graph, dist
    q = queue.Queue()
    s = convertToNumber(x0, y0)
    q.put(s)
    dist[s] = 0

    while not q.empty():
        u = q.get()
        x = u // MAX
        y = u % MAX

        for i in range(8):
            curX = x + dx[i]
            curY = y + dy[i]
            v = convertToNumber(curX, curY)
            if 1 <= curX <= MAX and 1 <= curY <= MAX and v in graph:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    if v == convertToNumber(x1, y1):
                        print(dist[v])
                        return
                    q.put(v)
    print(-1)


if __name__ == '__main__':
    x0, y0, x1, y1 = map(int, input().split())
    graph.add(convertToNumber(x0, y0))
    graph.add(convertToNumber(x1, y1))
    n = int(input())
    for i in range(n):
        r, a, b = map(int, input().split())
        for j in range(a, b+1):
            graph.add(convertToNumber(r, j))
    BFS(x0, y0, x1, y1)
