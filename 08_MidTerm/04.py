def calculateSum(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        return calculateSum(arr, 0, end + 1)
    else:
        ans += s[start: end + 1]
        print(arr[start:end + 1])
        return calculateSum(arr, start + 1, end)

if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = 0
        s = [0] * n
        for idx in range(n):
            if idx == 0:
                s[0] = arr[0]
            else:
                s[idx] = s[idx-1] ^ arr[idx]


