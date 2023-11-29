def generateSmallestBitString(n, h):
    s = ''
    for i in range(n-1, -1, -1):
        if i < h:
            s += '1'
        else:
            s += '0'
    return s


def shouldSwap(s, start, end):
    for i in range(start, end):
        if s[i] == s[end]:
            return False
    return True


def distinctPermutations(s, l, r):
    if l >= r:
        print("".join(s))
        return

    for i in range(l, r):
        check = shouldSwap(s, l, i)
        if check:
            s[l], s[i] = s[i], s[l]
            distinctPermutations(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        input()
        n, h = map(int, input().split())
        s = list(generateSmallestBitString(n, h))
        distinctPermutations(s, 0, len(s))