from timeit import default_timer as time

start = time()
Sum = 0
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		Sum += i

print(Sum)
print(time() - start)