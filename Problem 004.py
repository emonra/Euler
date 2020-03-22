from timeit import default_timer as time

start = time()
def IsPalindrome(number):
	if str(number) == str(number)[::-1]:
		return True
	else: return False

number = 0
for i in range(999, 900, -1):
	for j in range (999, 900, -1):
		if IsPalindrome(i*j):
			if i*j > number: number = i*j

print(number)
print(time() - start)