from timeit import default_timer as time

start = time()
start1 = start
def IsPandigital(Number):
	Number = str(Number)
	if len(Number) > 9:
		return False
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
	if count % 10000 == 0:
		print(count, time() - start1)
		start1 = time()
	if EndsArePandigital(Fib[2]):
		print(count)
		break


print(time() - start)