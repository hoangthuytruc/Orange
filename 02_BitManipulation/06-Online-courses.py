import sys
sys.setrecursionlimit(1000000)

def dfs(u):
    global cycle
    if check[u] == 0:
        check[u] = 1
        for v in graph[u]:
            dfs(v)
        check[u] = 2
        result.append(u)
    elif check[u] == 1:
        cycle = True


if __name__ == '__main__':
    n, k = map(int, input().split())
    main_courses = map(int, input().split())
    check = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    result = []
    cycle = False
    for i in range(1, n+1):
        requiredCourses = list(map(int, input().split()))
        if requiredCourses[0] != 0:
            for course in requiredCourses[1:]:
                graph[i].append(course)

    for i in main_courses:
        dfs(i)

    if cycle:
        print("-1")
    else:
        print(len(result))
        print(" ".join(map(str, result)))
