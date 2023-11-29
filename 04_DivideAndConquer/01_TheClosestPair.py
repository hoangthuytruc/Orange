import math
INF = 1e9

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return (x * x + y * y) ** 0.5


def bruteForce(points, left, right):
    min_dict = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dict + min(min_dict, distance(points[i], points[j]))
    return min_dict


def stripClosest(point_set, left, right, mid, dist_min):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda p: p.y)
    smallest = dist_min
    l = len(splitted_points)
    for i in range(0, l):
        for j in range(i + 1, l):
            if not (splitted_points[j].y - splitted_points[i].y) < smallest:
                break
            d = distance(splitted_points[i], splitted_points[j])
            smallest = min(smallest, d)
    return smallest


def minimalDistance(point_set, left, right):
    if right - left <= 3:
        return bruteForce(point_set, left, right)
    mid = (right + left) // 2
    dist_left = minimalDistance(point_set, left, mid)
    dist_right = minimalDistance(point_set, mid + 1, right)
    dist_min = min(dist_left, dist_right)
    return min(dist_min, stripClosest(point_set, left, right, mid, dist_min))


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            point_set = []
            for i in range(n):
                x, y = map(int, input().split())
                point_set.append(Point(x, y))
            point_set.sort(key=lambda point: point.x) 
            ans = minimalDistance(point_set, 0, n)
            print("{:.4f}".format(ans) if ans < 10000 else "INFINITY")