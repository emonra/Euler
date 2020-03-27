from timeit import default_timer as time

start = time()

def IsPrime(n):
	from math import sqrt
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return False
	return True

count = 0
for num in range (2,1000000):
	q=False
	num=str(num)
	for i in range(len(num)):
		if IsPrime(int(num[i:]+num[:i])):
			q=True
		else:
			q=False
			break
	if q:       
		count+=1            
		print(count,num)

print(time() - start)