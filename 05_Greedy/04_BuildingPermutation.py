if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    res = 0
    for i in range(1, n + 1):
        res += abs(i - numbers[i - 1])
    print(res)