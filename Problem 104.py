from timeit import default_timer as time

start = time()
def IsPandigital(Number):
	for i in range(1, 10):
		if Number.find(str(i)) == -1:
			return False
	return True


def EndsArePandigital(Number):
	Number = str(Number)
	if IsPandigital(Number[:9]) and IsPandigital(Number[-9:]):
		return True
	return False

Fib = [1, 1, 2]
count = 3
while True:
	count += 1
	Fib[0] = Fib[1]
	Fib[1] = Fib[2]
	Fib[2] = Fib[0] + Fib[1]
	"""checking pandigital-ness makes the script runs for more 
	than two and a half hours, which means it's not efficient"""
	if count % 10000 == 0:
		print(count, time() - start)
	if EndsArePandigital(Fib[2]):
		print(count)
		break


print(time() - start)