if __name__ == '__main__':
    n = int(input())
    log = list(map(int, input().split()))
    check = [0] * (n + 1)
    for x in log:
        check[x] = 1
    count = 1
    for i in range(n):
        if not check[i]:
            count += 1
    print(count)