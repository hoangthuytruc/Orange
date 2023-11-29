if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        if n % 2 == 0:
            print(0)
        else:
            ans = 0
            for j in range(0, n, 2):
                ans = ans ^ arr[j]
            print(ans)