import timeit
from math import floor
def d(x):
    DivisionSum = 0
    for i in range(1,floor(x/2)+1):
        if x % i == 0:
            DivisionSum += i
    return DivisionSum

SumOfAmicalble = 0
start = timeit.default_timer()
for count in range(10000):
    if count == d(d(count)) and count != d(count):
        SumOfAmicalble += count
elapsed = timeit.default_timer() - start
print(SumOfAmicalble)
print(elapsed)
