from timeit import default_timer as time

start = time()
number = pow(2,1000)
def DigitSum(number):
	Sum = 0
	for i in range(len(str(number))):
		Sum += int(str(number)[i])
	return Sum

print(DigitSum(number))
print(time() - start)