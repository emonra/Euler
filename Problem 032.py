from timeit import default_timer as time

startTime = time()

def IsPandigital(Number):
	Number = str(Number)
	for i in range(1, 10):
		if Number.find(str(i)) == -1:
			return False
	return True

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if IsPandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print(sum(p))
print(time() - startTime)