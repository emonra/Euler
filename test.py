import math
import time

def IsPrime(n):
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True

count = 0
num = 0
while True:
	num += 1
	if IsPrime(num):
		count += 1
		print(count, num)
	time.sleep(0.0001)