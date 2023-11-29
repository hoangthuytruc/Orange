def get(x, y, h, w):
    res = 0
    for i in range(x, x + h):
        for j in range(y, y + w):
            if a[i][j] == '1':
                res += 1
    return res


def B2D(x, y, h, w):
    if h == 0 or w == 0:
        return ""

    sum = get(x, y, h, w)

    if sum == 0:
        return "0"
    elif sum == h * w:
        return "1"

    s1 = B2D(x, y, (h + 1) // 2, (w + 1) // 2)
    s2 = B2D(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
    s3 = B2D(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
    s4 = B2D(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)

    return "D" + s1 + s2 + s3 + s4


def D2B(x, y, h, w):
    global string_it
    if h == 0 or w == 0:
        return

    c = stream[string_it]
    string_it += 1

    if c == '1':
        for i in range(x, x + h):
            for j in range(y, y + w):
                dest[i][j] = '1'
        return
    elif c == '0':
        for i in range(x, x + h):
            for j in range(y, y + w):
                dest[i][j] = '0'
        return

    D2B(x, y, (h + 1) // 2, (w + 1) // 2)
    D2B(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
    D2B(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
    D2B(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)


if __name__ == "__main__":
    line = input()
    while True:
        if line == '#':
            break
        line = line.split()
        h = int(line[1])
        w = int(line[2])
        x = line[0]
        iterator = 0
        stream = ""
        while True:
            line = input()
            if line == "#" or ' ' in line:
                break
            stream += line

        if x == 'B':
            a = [stream[i:i + w] for i in range(0, h * w, w)]
            print('D', end='')
            res = B2D(0, 0, h, w)
        else:
            print('B', end='')
            string_it = 0
            dest = [['0' for i in range(w)] for j in range(h)]
            D2B(0, 0, h, w)
            res = ''.join([''.join(line) for line in dest])

        print("%4d %3d" % (h, w))
        l = len(res)
        for i in range(l):
            print(res[i], end='')
            if (i + 1) % 50 == 0 or i == l - 1:
                print()