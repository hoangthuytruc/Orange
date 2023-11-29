if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n, m = map(int, input().split())
        count = 0
        ans = []
        while m:
            if m % 2 == 1:
                ans.append("({0}<<{1})".format(n, count))
            count += 1
            m = m // 2
        ans.reverse()
        print(" + ".join(ans))