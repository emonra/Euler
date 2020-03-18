from timeit import default_timer as time
from math import pow as pow

start = time()
def SumOfSquare(start, stop):
	Sum = 0
	for i in range(start, stop + 1):
		Sum = Sum + pow(i, 2)
	return Sum


def SquareOfSum(start, stop):
	Sum = 0
	for i in range(start, stop + 1):
		Sum += i
	return pow(Sum, 2)


print(SquareOfSum(1, 100) - SumOfSquare(1, 100))
print(time() - start)