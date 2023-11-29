class Question:
    def __init__(self, tests, point, time):
        self.tests = tests
        self.point = point
        self.time = time


K = []
def Knapsack(items, W):
    global K
    K = [[0] * (W + 1) for _ in items]
    for i in range(1, len(items)):
        for j in range(W + 1):
            if items[i].time > j:
                K[i][j] = K[i - 1][j]
            else:
                tmp1 = (items[i].point * items[i].tests) + K[i - 1][j - items[i].time]
                tmp2 = K[i - 1][j]
                K[i][j] = max(tmp1, tmp2)

    return K[len(items) - 1][W]


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        N, W = map(int, input().split())
        items = []
        items.append(Question(0, 0, 0))
        for i in range(N):
            c, p, t = map(int, input().split())
            items.append(Question(c, p, t))
        ans = Knapsack(items, W)
        print(ans)