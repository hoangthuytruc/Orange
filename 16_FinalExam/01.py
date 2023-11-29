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


if __name__ == '__main__':
    while True:
        line = input().split()
        if line[0] == '-1' and line[1] == '*':
            break
        else:
            n = int(line[0])
            s = line[1]
            prefix = [0] * len(s)
            KMPPreprocess(s, prefix)
            maxCommonSubstring = prefix[len(s) - 1]
            if maxCommonSubstring == 0 or maxCommonSubstring == (len(s) - 1):
                print(n // len(s))
            else:
                print((abs(n - maxCommonSubstring)) // (len(s) - maxCommonSubstring))