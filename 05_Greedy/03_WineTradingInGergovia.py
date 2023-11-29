if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            wines = list(map(int, input().split()))
            res = x = 0
            for w in wines:
                res += abs(x)
                x += w
            print(res)