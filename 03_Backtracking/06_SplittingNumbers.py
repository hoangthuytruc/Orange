if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            a = b = 0
            idx = 0
            count = 0
            while n != 0:
                if n & 1 == 1:
                    if count % 2 == 0:
                        b = b | (1 << idx)
                    else:
                        a = a | (1 << idx)
                    count += 1
                idx += 1
                n >>= 1
            print(b, a)