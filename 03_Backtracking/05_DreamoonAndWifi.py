finalPositionInS1 = 0
cases = 0
possibleCases = 0


def recursive(idx, currentPosition):
    global finalPositionInS1, cases, possibleCases

    if idx == len(s2):
        if currentPosition == finalPositionInS1:
            possibleCases += 1
        cases += 1
        return

    if s2[idx] != '+':
        # replace '?' with '-'
        recursive(idx + 1, currentPosition - 1)
    if s2[idx] != '-':
        # replace '?' with '+'
        recursive(idx + 1, currentPosition + 1)


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    for c in s1:
        if c == '+':
            finalPositionInS1 += 1
        else:
            finalPositionInS1 -= 1
    recursive(0, 0)
    print("{:.10f}".format(possibleCases/cases))

