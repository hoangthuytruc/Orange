def KMPPreprocess(p, prefix):
    prefix[0] = 0
    m = len(p)
    j = 0
    i = 1
    while i < m:
        if p[i] == p[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1


def KMPSearch(t, p, prefix):
    n = len(t)
    m = len(p)
    i = j = 0
    count = 0
    while i < n:
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = prefix[j - 1]
        elif i < n and p[j] != t[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return count


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        s = "".join(list(map(str, input().split())))
        p = input()
        prefix = [0] * len(p)
        KMPPreprocess(p, prefix)
        ans = KMPSearch(s, p, prefix)
        print("Case {0}: {1}".format(i + 1, ans))
