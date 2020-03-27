from timeit import default_timer as time
from math import sqrt as sqrt

start = time()
def IsPrime(n):
	from math import sqrt
	if n < 2: return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True
	
i = 0
number = 1
while i <= 10000:
	i += 1
	number += 1
	while not(IsPrime(number)):
		number += 1

print(number)
print(time() - start)