from timeit import default_timer as time

start = time()
def factorial(number):
	fact = 1
	for i in range(1, number + 1):
		fact = fact * i
	return fact


CuriousSum = 0
for i in range(10, 10000000):
	sum = 0
	digits = list(str(i))
	for j in digits:
		sum += factorial(int(j))
	if i == sum:
		CuriousSum += i

print(CuriousSum)
print(time() - start)