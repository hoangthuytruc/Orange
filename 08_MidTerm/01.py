if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        a = input()
        sum = 0
        for idx in range(len(a)):
            sum += int(a[idx])
        reversed = 0
        while a > 0:
            remainder = a % 10
            reversed = reversed * 10 + remainder
            a = a // 10