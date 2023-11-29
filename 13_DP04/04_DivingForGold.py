class Gold:
    def __init__(self, time, value):
        self.time = time
        self.value = value


K = []
def Knapsack(items, T, W):
    global K
    K = [[0] * (T + 1) for _ in items]
    for i in range(1, len(items)):
        for j in range(T + 1):
            i_time = 3 * W * items[i].time
            if i_time > j:
                K[i][j] = K[i - 1][j]
            else:
                tmp1 = items[i].value + K[i - 1][j - i_time]
                tmp2 = K[i - 1][j]
                K[i][j] = max(tmp1, tmp2)

    return K[len(items) - 1][T]


def printItems(items, T, W):
    count = 0
    res = []
    for i in range(len(items) - 1, 0, -1):
        if K[i][T] != K[i - 1][T]:
            count += 1
            res.append(items[i])
            T -= 3 * W * items[i].time
    print(count)
    for i in range(len(res) - 1, -1, -1):
        print(res[i].time, res[i].value)


if __name__ == '__main__':
    tc = 0
    while True:
        try:
            tc += 1
            if tc > 1:
                 input()

            T, W = map(int, input().split())
            items = []
            items.append(Gold(0, 0))
            n = int(input())
            for _ in range(n):
                t, d = map(int, input().split())
                items.append(Gold(t, d))
            ans = Knapsack(items, T, W)

            if tc > 1:
                print()
                
            print(ans)
            printItems(items, T, W)
        except:
            break