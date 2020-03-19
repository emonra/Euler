from timeit import default_timer as time
import math

start = time()
num = 1
triangle_number = 1
Max = 0
while True:
	amount = 0
	num += 1
	triangle_number += num
	for i in range(1, math.ceil(math.sqrt(triangle_number))):

		if triangle_number % i == 0:		
			amount += 2 # divider and share

	if Max < amount: 
		Max = amount
		print(amount)
	if amount >= 500:
		break


print(triangle_number)
print(time() - start)