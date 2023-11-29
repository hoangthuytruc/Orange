MAX = 1000001


def changeCoin(n):
    if n < MAX:
        return preComputedArr[n]
    return changeCoin(n // 2) + changeCoin(n // 3) + changeCoin(n // 4)


if __name__ == '__main__':
    preComputedArr = [-1] * MAX
    preComputedArr[0] = 0
    for i in range(MAX):
        tmp = preComputedArr[i // 2] + preComputedArr[i // 3] + preComputedArr[i // 4]
        preComputedArr[i] = max(tmp, i)

    while True:
        try:
            n = int(input())
            print(changeCoin(n))

        except EOFError:
            break
