from timeit import default_timer as time
from math import gcd
start = time()
n = 0
Min = 4503599627370517
Sum = 0
while (time() - start) < 10:
	n += 1
	temp = (1504170715041707 * n) % 4503599627370517
	if temp < Min:
		Min = temp
		Sum += temp
		print(n, time() - start, temp, Sum)
	if time() - start > 20:
		break

