from timeit import default_timer as time
from math import sqrt as sqrt

start = time()
def IsPrime(n):
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True

Sum = 0
for i in range(2, 2000000):
	if IsPrime(i): Sum += i

print(Sum)
print(time() - start)