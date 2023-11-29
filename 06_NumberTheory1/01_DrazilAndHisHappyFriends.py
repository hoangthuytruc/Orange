def gcd(a, b):
   while b != 0:
      r = a % b
      a = b
      b = r
   return a

n, m = map(int, input().split())
b, *boys = list(map(int, input().split()))
g, *girls = list(map(int, input().split()))
happy_boys = [False] * n
happy_girls = [False] * m

for x in boys:
   happy_boys[x] = True

for x in girls:
   happy_girls[x] = True

res = n + m - b - g
lcm = n * m // gcd(n, m)

for i in range(2 * lcm):
   if happy_boys[i % n] + happy_girls[i % m] == 1:
      happy_boys[i % n] = happy_girls[i % m] = True
      res -= 1

print('Yes' if res == 0 else 'No')