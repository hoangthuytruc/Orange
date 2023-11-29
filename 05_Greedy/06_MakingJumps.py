import queue

graph = [[False for _ in range(10)] for _ in range(10)]
direct = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
          (1, -2), (1, 2), (2, -1), (2, 1)]


def DFS(x, y):
    global graph
    path = 0
    graph[x][y] = False
    for i in range(8):
        ux = x + direct[i][0]
        uy = y + direct[i][1]
        if 0 <= ux < 10 and 0 <= uy < 10 and graph[ux][uy]:
            path = max(path, DFS(ux, uy))
    graph[x][y] = True
    return path + 1


def main():
    global graph

    test = 1
    while True:
        area = 0
        graph = [[False for _ in range(10)] for _ in range(10)]

        case = list(map(int, input().split()))
        n = case.pop(0)
        if n == 0:
            break

        start_col = case[0]
        for _ in range(n):
            area += case[1]
            for i in range(case[1]):
                graph[_][case[0] + i] = True
            case = case[2:]

        result = area - DFS(0, start_col)
        if result == 1:
            print("Case {}, {} square can not be reached.".format(test, result))
        else:
            print("Case {}, {} squares can not be reached.".format(test, result))
        test += 1


if __name__ == "__main__":
    main()