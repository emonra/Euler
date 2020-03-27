from timeit import default_timer as time

def IsPrime(n):
	from math import sqrt
	if n < 2: return False
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True


def TruncatableFromLeft(Number):
	from math import log10, floor
	if Number < 10: return False
	for i in range(floor(log10(Number,)), 0, -1):
		temp = Number % pow(10,i)
		if not(IsPrime(temp)):
			return False
	return True


def TruncatableFromRight(Number):
	from math import log10, floor
	if Number < 10: return False
	for i in range(1, floor(log10(Number)) + 1):
		temp = (Number - Number % pow(10,i)) / pow(10, i)
		if not(IsPrime(temp)):
			return False
	return True


def main():
	start = time()
	count = 0
	n = 9
	Sum = 0
	while count < 11:
		n += 2
		if IsPrime(n):
			if(TruncatableFromLeft(n) and TruncatableFromRight(n)):
				count += 1
				Sum += n
	print(Sum)
	print(time() - start)


if __name__ == "__main__":
	main()