from timeit import default_timer as time
from time import sleep as sleep

start = time()

def CollatzLen(num):
	Len = 0
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3 * num + 1
		Len += 1
	return Len


Max = 0
MaxCollatz = 0
for i in range(500001, 1000000, 2):
	if CollatzLen(i) > Max:
		Max = CollatzLen(i)
		MaxCollatz = i

print(MaxCollatz)
print(time() - start)