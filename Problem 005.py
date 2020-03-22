from timeit import default_timer as time

start = time()

def IsMultiple(Start, Stop, Number):
	for i in range(Start, Stop+1):
		if Number % i != 0:
			return False
	return True


i = 2520*13*17*19
#the numbers are just math trick (2520 is LCM of 1 to 10 and others are primes lower than 20)
while True :
	if IsMultiple(1, 20, i):
		print(i)
		break
	i += 2520*13*17*19

print(time() - start)