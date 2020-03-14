def IsPalindrome(number):
	if str(number) == str(number)[::-1]:
		return True
	else: return False


Sum = 0

for i in range(1000000):
	if (IsPalindrome(i) == True) and (IsPalindrome(str(bin(i))[2::1]) == True):
		Sum += i



print(Sum)