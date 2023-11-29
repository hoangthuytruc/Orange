if __name__ == '__main__':
    while True:
        s = input()
        if s[0] == '0':
            break
        else:
            n = len(s)
            result = [0] * (n + 1)
            s = '0' + s
            result[0] = 1
            for i in range(1, n + 1):
                result[i] = result[i - 1]
                if int(s[i-1] + s[i]) <= 26:
                    result[i] += result[i - 2]
            print(result[n])