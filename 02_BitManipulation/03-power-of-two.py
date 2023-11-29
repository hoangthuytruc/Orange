def isPowerOfTwo(a):
    return a & (a-1) == 0

def checkSubSet(s):
    if len(s) == 0:
        return False

    res = s[0]
    for k in range(0, len(s)):
        res &= s[k]
        if isPowerOfTwo(res):
            return True
    return False

if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        numbers = list(map(int, input().split()))
        flag = False
        for j in range(32):
            subSet = []
            for e in numbers:
                if (e >> j) & 1 == 1:
                    subSet.append(e)
            if checkSubSet(subSet):
                flag = True
                break
        print("YES" if flag else "NO")