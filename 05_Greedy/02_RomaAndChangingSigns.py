if __name__ == '__main__':
    n, k = map(int, input().split())
    incomes = list(map(int, input().split()))
    min_income = 100000
    sum = 0
    for x in incomes:
        if x < 0 and k > 0:
            sum += abs(x)
            min_income = min(min_income, abs(x))
            k -= 1
        else:
            sum += x
            min_income = min(min_income, abs(x))

    if k % 2 != 0:
        sum -= 2 * min_income
    print(sum)