from math import ceil, log2
INF = 10**9


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] | segtree[2 * index + 2]


def orRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = (left + right) // 2
    return orRange(segtree, left, mid, fr, to, 2 * index + 1) | orRange(segtree, mid + 1, right, fr, to, 2 * index + 2)


def updateTree(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left + right) // 2
    if pos <= mid:
        updateTree(segtree, a, left, mid, 2 * index + 1, pos, value)
    else:
        updateTree(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] | segtree[2 * index + 2]


if __name__ == '__main__':
    n, q = map(int, input().split())

    # build tree
    h = ceil(log2(n))
    sizeTree = 2 * (2 ** h) - 1
    segtree = [INF] * sizeTree
    a = list(map(int, input().split()))
    buildTree(a, segtree, 0, n - 1, 0)

    # query
    for _ in range(q):
        pos, value = map(int, input().split())
        updateTree(segtree, a, 0, n - 1, 0, pos - 1, value)
        res = orRange(segtree, 0, n - 1, 0, n - 1, 0)
        print(res)