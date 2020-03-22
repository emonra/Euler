from timeit import default_timer as time

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

start = time()
print(SumOfDigits(Factorial(100)))
print(time() - start)