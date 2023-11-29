dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def dfs(sx, sy, step, bits):
    global octaves, graph, n, visited
    visited[sx][sy] = True
    bits |= 1 << (sx * n + sy)

    if step == 8:
        octaves.add(bits)
    else:
        for i in range(4):
            x, y = sx + dx[i], sy + dy[i]
            if x in range(n) and y in range(n) and not visited[x][y] and graph[x][y] == 'X':
                dfs(x, y, step + 1, bits)
    bits &= ~(1 << (sx * n + sy))
    visited[sx][sy] = False


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        visited = [[False] * n for _ in range(n)]
        graph = []
        octaves = set()
        for i in range(n):
            graph.append(input())
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    bits = 0
                    dfs(i, j, 1, bits)
        print(len(octaves))