from math import ceil, log2
INF = 10**9


def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] * segtree[2 * index + 2]


def multiplyRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 1
    mid = (left + right) // 2
    return multiplyRange(segtree, left, mid, fr, to, 2 * index + 1) * multiplyRange(segtree, mid + 1, right, fr, to, 2 * index + 2)


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
    segtree[index] = segtree[2 * index + 1] * segtree[2 * index + 2]


if __name__ == '__main__':
    while True:
        try:
            line = input().split()
            n = int(line[0])
            k = int(line[1])
            a = list(map(int, input().split()))

            h = ceil(log2(n))
            sizeTree = 2 * (2 ** h) - 1
            segtree = [INF] * sizeTree
            buildTree(a, segtree, 0, n - 1, 0)

            # query
            ans = []
            for i in range(k):
                query = input().split()
                if query[0] == 'C':
                    pos = int(query[1])
                    value = int(query[2])
                    updateTree(segtree, a, 0, n - 1, 0, pos - 1, value)
                else:
                    res = multiplyRange(segtree, 0, n - 1, int(query[1]) - 1, int(query[2]) - 1, 0)
                    if res == 0:
                        ans.append("0")
                    else:
                        ans.append("+" if res > 0 else "-")
            print("".join(ans))

        except EOFError:
            break