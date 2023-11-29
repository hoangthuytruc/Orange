if __name__ == '__main__':
    N = int(input())
    bits = list(map(int, input().split()))
    Q = int(input())
    count0 = [0] * (N+1)
    for i in range(1, N + 1):
        if bits[i-1] == 0:
            count0[i] = count0[i-1] + 1
        else:
            count0[i] = count0[i-1]

    for i in range(Q):
        L, R = map(int, input().split())
        n0 = count0[R] - count0[L-1]
        n1 = (R - L + 1) - n0
        xor = n1 % 2
        print(xor, n0)
