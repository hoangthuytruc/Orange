def backtracking(s, ans, idx):
    if len(ans) == 6:
        print(" ".join(map(str, ans)))
        return

    for i in range(idx, len(s)):
        ans.append(s[i])
        backtracking(s, ans, i + 1)
        ans.pop(-1)


if __name__ == '__main__':
    while True:
        numbers = list(map(int, input().split()))
        k = numbers[0]
        ans = []
        if k == 0:
            break
        else:
            backtracking(numbers[1:], ans, 0)