from timeit import default_timer as time

start = time()
Number = 600851475143
def IsPrime(n):
	from math import sqrt
	if n < 2: return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True

for x in range(int(sqrt(Number)), 0, -1):
	if IsPrime(x) and Number % x == 0:
		print(x)
		break


print(time() - start)