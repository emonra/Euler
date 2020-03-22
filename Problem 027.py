from timeit import default_timer as time
from math import sqrt as sqrt
start = time()

def IsPrime(number):
	if number < 0:
		return False
	for i in range(2, int(sqrt(number) + 1)):
		if number % i == 0: 
			return False
	return True


aLast = 0
bLast = 0
nMax = 0
aMax = 0
bMax = 0
for a in range(-999, 1000):
	for b in range(-1000, 1001):
		n = -1
		Expression = b
		while IsPrime(Expression):
			n += 1
			aLast = a
			bLast = b
			Expression = pow(n,2) + a*n + b
		if n > nMax:
			nMax = n
			aMax = aLast
			bMax = bLast

print(aMax * bMax)
print(time() - start)