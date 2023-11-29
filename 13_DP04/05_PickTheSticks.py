import math

class Gold:
    def __init__(self, length, value):
        self.length = length
        self.value = value


K = []


def Knapsack(items, L):
    global K
    K = [[0] * (L + 1) for _ in items]
    for i in range(1, len(items)):
        for j in range(L + 1):
            i_length = math.ceil(items[i].length / 2)
            if i_length > j:
                K[i][j] = max(K[i - 1][j], items[i].value)
            else:
                tmp1 = K[i - 1][j]
                if math.ceil(items[i - 1].length / 2) <= j - i_length:
                    tmp2 = items[i].value + K[i - 1][j - i_length]
                    K[i][j] = max(tmp1, tmp2)
                else:
                    K[i][j] = max(items[i].value, tmp1)
    print(K)
    return K[len(items) - 1][L]


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        input()
        items = [Gold(0, 0)]
        N, L = map(int, input().split())
        for _ in range(N):
            a, v = map(int, input().split())
            items.append(Gold(a, v))
        print("Case #{0}: {1}".format(i + 1, Knapsack(items, L)))