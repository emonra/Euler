from timeit import default_timer as time

#fuction return the index of the digits that make the sum go over max_sum
#returns -1 if max sum is lower than max_sum
def MaxConsecutiveSum(number, consecutive_digits, max_sum):
	from math import log10, ceil
	temp = str(number)
	for i in range(ceil(log10(number)) + 1 - consecutive_digits):
		digits_sum = 0
		for j in range(consecutive_digits):
			digits_sum += int(temp[i + j])
			if digits_sum > max_sum:
				return i+j
	return -1



def main():
	from math import log10, ceil
	count = 0
	n = pow(10, 19)
	while n < pow(10, 20) - 1:
		index = MaxConsecutiveSum(n, 3, 9)
		if index == -1:
			count += 1
			print(count, n)
			n += 1
		else:
			n += pow(10, ceil(log10(n)) - 1 - index)

		


if __name__ == "__main__":
	main()