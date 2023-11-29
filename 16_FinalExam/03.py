result = []


def lowerBound(a, sub, n, x):
    left = 0
    right = n
    pos = right
    while left < right:
        mid = left + (right - left) // 2
        index = sub[mid]
        if a[index] >= x:
            pos = mid
            right = mid
        else:
            left = mid + 1

    return pos


def LIS(a):
    length = 1
    result.append(0)
    for i in range(1, len(a)):
        if a[i] <= a[result[0]]:
            result[0] = i
        elif a[i] > a[result[length - 1]]:
            result.append(i)
            length += 1
        else:
            pos = lowerBound(a, result, length, a[i])
            result[pos] = i
    return length


if __name__ == '__main__':
    tc = int(input())

    for i in range(tc):
        a = int(input())
        if a == 0:
            print(0)
        else:
            result = []
            arr = []
            for j in range(a):
                k = int(input())
                arr.append(k)
            ans = LIS(arr)
            print(ans)