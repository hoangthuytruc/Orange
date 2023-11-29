def canFill(capacity, a, m):
  container = 0
  numberOfContainer = 0
  for i in range(len(a)):
    if a[i] > capacity:
      return False
    if container + a[i] > capacity:
      container = 0
    if container == 0:
      numberOfContainer += 1
    if numberOfContainer > m:
      return False
    container += a[i]
  return True
def binarySearch(a, total, m):
  low = 0
  high = total
  res = -1
  while low <= high:
    mid = (low + high) // 2
    if canFill(mid, a, m):
      res = mid
      high = mid - 1
    else:
      low = mid + 1
  return res
while True:
  try:
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    total = sum(c)
    print(binarySearch(c, total, m))
  except EOFError:
    break