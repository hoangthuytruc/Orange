INF = 10**9

def sumOfDigits(n):
    s = 0
    while n:
        s += n % 10
        n = n // 10
    return s


def hash(n):
    return n ^ sumOfDigits(n)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    dic = dict()
    for e in numbers:
        h = hash(e)
        if h in dic.keys():
            dic[h] += 1
        else:
            dic[h] = 1
    if len(dic.keys()) == n:
        print(max(dic.keys()), 0)
    else:
        maxCollision = -1
        collision = 0
        minimum = INF
        for k in dic.keys():
            if dic[k] > 1:
                collision += dic[k] - 1
                maxCollision = max(maxCollision, dic[k])
        for k in dic.keys():
            if dic[k] == maxCollision:
                minimum = min(minimum, k)
        print(minimum, collision)