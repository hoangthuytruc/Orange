import sys


def Scanner():
    for line in sys.stdin.readlines():
        for token in line.split():
            if token:
                yield token


scanner = Scanner()


def count_bracket(st):
    brackets = 0
    for c in st:
        if c == '(':
            brackets += 1
        elif c == ')':
            brackets -= 1
    return brackets


def get_integer(it):
    temp = ''
    while exp[it].isdigit() or exp[it] == '-':
        temp += exp[it]
        it += 1
    return int(temp)


def left_child(it):
    while exp[it].isdigit() or exp[it] == '-':
        it += 1

    if it + 1 >= len(exp):
        return -1

    if not (exp[it + 1].isdigit() or exp[it + 1] == '-'):
        return -1
    return it + 1


def right_child(it):
    while exp[it].isdigit() or exp[it] == '-':
        it += 1

    brackets = 1
    it += 1
    if it >= len(exp):
        return -1

    while brackets > 0:
        if exp[it] == '(':
            brackets += 1
        elif exp[it] == ')':
            brackets -= 1
        it += 1

    if it + 1 >= len(exp):
        return -1

    if not (exp[it + 1].isdigit() or exp[it + 1] == '-'):
        return -1
    return it + 1


def check(it, target, current):
    if it >= len(exp):
        return False

    if (exp[it].isdigit() or exp[it] == '-'):
        current += get_integer(it)

    left = left_child(it)
    right = right_child(it)

    if left == -1 and right == -1:
        return (target == current)

    left_path = False
    right_path = False

    if left != -1:
        left_path = check(left, target, current)
    if right != -1:
        right_path = check(right, target, current)

    return left_path or right_path


def remove_space(s):
    return ''.join(s.split())


if __name__ == '__main__':
    while True:
        try:
            num = int(next(scanner))
        except:
            break

        exp = ''
        brackets = 0
        while True:
            try:
                temp = next(scanner)
            except:
                break
            brackets += temp.count('(') - temp.count(')')
            exp += temp
            if brackets == 0:
                break

        # print(num, exp)
        if check(1, num, 0):
            print('yes')
        else:
            print('no')

