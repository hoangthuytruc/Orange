if __name__ == '__main__':
    total = 0
    tank = 0
    lastPivot = 0
    n = 0
    leakCount = 0
    while True:
        split = input().split()
        pivot = float(split[0])
        total += (n / 100.0 + leakCount) * (pivot - lastPivot)
        tank = max(tank, total)
        lastPivot = pivot
        if split[1] == 'Fuel':
            n = float(split[3])
            if n == 0:
                exit()
        elif split[1] == 'Leak':
            leakCount += 1
        elif split[1] == 'Gas':
            total = 0
        elif split[1] == 'Mechanic':
            leakCount = 0
        else:
            print('{:.3f}'.format(tank))
            total = 0
            lastPivot = 0
            leakCount = 0
            n = 0
            tank = 0
