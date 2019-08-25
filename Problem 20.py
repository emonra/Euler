import timeit

def Factorial(n):
    fact = 1
    for count in range(1,n+1):
        fact = fact * count
    return fact

def SumOfDigits(x):
    StringOfNum = str(x)
    SumOfSubString = 0
    for j in StringOfNum:
        SumOfSubString = SumOfSubString + int(j)
    return SumOfSubString

start = timeit.default_timer()
print(SumOfDigits(Factorial(100)))
elapsed = timeit.default_timer() - start
print(elapsed)