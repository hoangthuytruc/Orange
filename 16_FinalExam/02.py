from math import ceil, log2
INF = 10**9


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = min(segtree[2 * index + 1], segtree[2 * index + 2])


def updateTree(a, segtree, lazy, left, right, fr, to, delta, index):
    if left > right:
        return
    if lazy[index] != 0:
        segtree[index] += lazy[index]
        a[index] += lazy[index]
        if left != right:
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0

    if fr > right or to < left:
        return

    if fr <= left and right <= to:
        segtree[index] += delta
        if left != right:
            lazy[2 * index + 1] += delta
            lazy[2 * index + 2] += delta
        return

    mid = (left + right) // 2
    updateTree(a, segtree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    updateTree(a, segtree, lazy, mid + 1, right, fr, to, delta, 2 + index + 1)
    segtree[index] = min(segtree[2 * index + 1], segtree[2 * index + 2])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    # build tree
    h = ceil(log2(n))
    sizeTree = 2 * (2 ** h) - 1
    segtree = [INF] * sizeTree
    lazy = [0] * sizeTree
    buildTree(a, segtree, 0, n - 1, 0)

    # update
    q = int(input())
    for i in range(q):
        x = int(input())
        updateTree(a, segtree, lazy, x + 1, )