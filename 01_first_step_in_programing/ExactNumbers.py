n = int(input())
k = int(input())
sum = (5**n * 2**k) / (5**(k // n) * 2 ** (n % k))
print("%.10f" % sum)

