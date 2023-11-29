import math


K = []
def Knapback(coins, W):
    global K
    K = [[0] * (W + 1) for _ in coins]
    for i in range(1, len(coins)):
        for j in range(W + 1):
            if coins[i] > j:
                K[i][j] = K[i - 1][j]
            else:
                tmp1 = coins[i] + K[i - 1][j - coins[i]]
                tmp2 = K[i - 1][j]
                K[i][j] = max(tmp1, tmp2)
    return K[len(coins) - 1][W]


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        coins = list(map(int, input().split()))
        coins.insert(0, 0)
        sumCoins = sum(coins)
        W = math.ceil(sumCoins / 2)
        maxA = Knapback(coins, W)
        print(abs(sumCoins - maxA * 2))