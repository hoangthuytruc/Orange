from sys import stdin, stdout

INF = int(1e9)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return x * x + y * y


def bruteForce(point_set, left, right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(point_set[i], point_set[j]))
    return min_dist


def stripClosest(point_set, left, right, mid, min_dist):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if (point_set[i].x - point_mid.x) ** 2 <= min_dist:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda point: point.y)
    l = len(splitted_points)
    smallest = INF
    for i in range(l):
        for j in range(i + 1, l):
            if (splitted_points[i].y - splitted_points[j].y) ** 2 >= min_dist:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)
    return smallest


def closestUtil(point_set, left, right):
    if right - left <= 3:
        return bruteForce(point_set, left, right)

    mid = (left + right) // 2
    dist_left = closestUtil(point_set, left, mid)
    dist_right = closestUtil(point_set, mid + 1, right)
    dist_min = min(dist_left, dist_right)

    return min(dist_min, stripClosest(point_set, left, right, mid, dist_min))


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

pref = [0]
for i in range(n):
    pref.append(pref[i] + a[i])

point_set = []
for i in range(n):
    point_set.append(Point(i, pref[i + 1]))

ans = closestUtil(point_set, 0, n)
stdout.write(str(ans))