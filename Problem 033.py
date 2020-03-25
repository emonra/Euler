from timeit import default_timer as time
from math import gcd
from time import sleep

start = time()
def LowestCommonTerms(numerator, denominator):
	while gcd(numerator, denominator) != 1:
		tempGcd = gcd(numerator, denominator)
		numerator //= tempGcd
		denominator //= tempGcd
	return numerator, denominator

#this only works for 2 digit numbers because of janky hacks
def IsCurious(numerator, denominator):
	temp = numerator / denominator
	numerator = str(numerator)
	denominator = str(denominator)
#i'm too tired to figure out how to do it properly
	if denominator.find(numerator[1]) != -1:
		denominator = denominator.replace(numerator[1], "", 1)
		numerator = numerator.replace(numerator[1], "", 1)
		if temp == int(numerator) / int(denominator):
			return True
	return False

Product = [1, 1]
for num in range(10, 100):
	for denom in range(num + 1, 100):
		if num % 10 and denom % 10:
			if IsCurious(num, denom):
				Product[0] *= num
				Product[1] *= denom


print(LowestCommonTerms(Product[0], Product[1]))
print(time() - start)
