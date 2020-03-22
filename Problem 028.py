from timeit import default_timer as time

start = time()
Number = 1 
Sum = 1
for increment in range(2, 1001, 2):
	for i in range(4):
		Number += increment
		Sum += Number

print(Sum)
print(time() - start)