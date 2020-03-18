from timeit import default_timer as time

start = time()
Fib = [1, 2, 3]
Sum = 0
while Fib[2] < 4000000:
	if Fib[2] % 2 == 0:
		Sum += Fib[2]
	Fib[0] = Fib[1]
	Fib[1] = Fib[2]
	Fib[2] = Fib[0] + Fib[1]
print(Sum)
print(time() - start)