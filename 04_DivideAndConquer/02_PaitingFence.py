import sys
sys.setrecursionlimit(10000)


def strokesNeeded(left, right, paintedHeight):
    if left > right:
        return 0

    minHeightIdx = left + a[left:right+1].index(min(a[left:right+1]))
    allVerticals = right - left + 1
    horizontals = a[minHeightIdx] - paintedHeight + strokesNeeded(left, minHeightIdx - 1, a[minHeightIdx]) + strokesNeeded(minHeightIdx + 1, right, a[minHeightIdx])

    return min(allVerticals, horizontals)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(strokesNeeded(0, n - 1, 0))