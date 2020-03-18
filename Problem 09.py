from timeit import default_timer as time

start = time()
def IsPythagorean(a, b, c):
	if pow(a, 2) + pow(b, 2) == pow(c, 2):
		return True
	return False


for c in range(500, 0, -1):
	for b in range(c - 1, 0, -1):
		a = 1000 - b - c
		if IsPythagorean(a, b, c):
			print(a, b, c)
			print(a * b * c)
			break

print(time() - start)