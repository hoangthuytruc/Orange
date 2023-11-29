def permutation(c, a, b, j, minn, ans):
    for i in range(5):
        if b[i]:
            a[j] = i
            b[i] = False
            if j == 4:
                check(c, a, minn, ans)
            else:
                permutation(c, a, b, j + 1, minn, ans)
            b[i] = True


def check(c, a, minn, ans):
    num = abs(c[a[0]] * c[a[3]] - c[a[1]] * c[a[2]])
    denom = c[a[1]] * c[a[3]]

    if cmp(num, denom, minn[0], minn[1]):
        minn[0] = num
        minn[1] = denom
        for i in range(4):
            ans[i] = a[i]


def cmp(num, denom, _num, _denom):
    return num * _denom < _num * denom


if __name__ == '__main__':

    a = [i for i in range(5)]
    ans = [0 for _ in range(4)]
    b = [True] * 5
    c = list(map(int, input().split()))
    minn = [1000000, 1]

    permutation(c, a, b, 0, minn, ans)
    print(" ".join(map(str, ans)))