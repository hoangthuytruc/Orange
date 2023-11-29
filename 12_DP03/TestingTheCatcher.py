result = []


def upperBound(a, sub, n, x):
    left = 0
    right = n
    pos = right
    while left < right:
        mid = left + (right - left) // 2
        index = sub[mid]
        if a[index] >= x:
            left = mid + 1
        else:
            pos = mid
            right = mid
    return pos


def LIS(a):
    length = 1
    result.append(0)
    for i in range(1, len(a)):
        if a[i] > a[result[0]]:
            result[0] = i
        elif a[i] <= a[result[length - 1]]:
            result.append(i)
            length += 1
        else:
            pos = upperBound(a, result, length, a[i])
            result[pos] = i
    return length


if __name__ == '__main__':
    tc = 0
    while True:
        a = int(input())
        if a == -1:
            break
        else:
            tc += 1
            result = []
            arr = []
            arr.append(a)
            while True:
                b = int(input())
                if b == -1:
                    ans = LIS(arr)
                    if tc != 1:
                        print()
                    print("Test #{0}:".format(tc))
                    print("  maximum possible interceptions: {0}".format(ans))
                    break
                else:
                    arr.append(b)