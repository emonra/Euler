from math import floor
from timeit import default_timer as time

def d(x):
    DivisionSum = 0
    for i in range(1,floor(x/2)+1):
        if x % i == 0:
            DivisionSum += i
    return DivisionSum

start = time()
abundants = set(i for i in range(1,28124) if d(i) > i)

def abundantsum(i):
    return any(i-a in abundants for a in abundants)

print(sum(i for i in range(1,28124) if not abundantsum(i)))
print(time()-start)
