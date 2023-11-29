def countBit(a):
    count = 0
    while a:
        if a % 2 == 1:
            count += 1
        a //= 2
    return count


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n, k = map(int, input().split())
        dishes = list()
        for i in range(n):
            dish = input()
            a = 0
            # convert to string of bit
            for j in range(k):
                if dish[j] == '1':
                    a = a | (1 << k-1-j)
            dishes.append(a)
        ans = k
        for i in range(1, 1 << k):
            isSelected = True
            for j in range(n):
                if (dishes[j] & i) == 0:
                    isSelected = False
            if isSelected:
                tmp = countBit(i)
                ans = min(ans, tmp)
        print(ans)