MAX = 2000
L = [[-1] * (MAX + 1) for _ in range(MAX + 1)]


def LCS(s1, s2, m, n):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        s1 = list(map(int, input().split()))
        ans = 0
        while True:
            s2 = list(map(int, input().split()))
            if s2[0] == 0:
                break
            else:
                ans = max(ans, LCS(s1, s2, len(s1), len(s2)))
        print(ans - 1)