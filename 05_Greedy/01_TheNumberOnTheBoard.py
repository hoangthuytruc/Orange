if __name__ == '__main__':
    k = int(input())
    n = input()
    sum = 0
    arr = []
    for x in n:
        tmp = int(x)
        sum += tmp
        arr.append(tmp)
    arr.sort()
    ans = 0
    for x in arr:
        if sum < k:
            ans += 1
            sum += 9 - x
    print(ans)