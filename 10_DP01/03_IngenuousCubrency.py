def changeCubes(total, cubes, n):
    result = [0] * (total + 1)
    result[0] = 1
    for i in range(n):
        for j in range(cubes[i], total + 1):
            result[j] += result[j - cubes[i]]
    return result


if __name__ == '__main__':
    cubes = []
    for i in range(1, 22):
        cubes.append(pow(i, 3))

    maxN = 10000
    res = changeCubes(maxN, cubes, 21)
    while True:
        try:
            n = int(input())
            print(res[n])
        except EOFError:
            break