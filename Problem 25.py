from timeit import default_timer as time

start = time()

def F(n):
    n_0=0
    n_1=1
    n_2=1
    for count in range(3,n+1):
        n_0 = n_1 + n_2
        n_2 = n_1
        n_1 = n_0
    return n_0

count = 3

while len(str(F(count))) < 1000:
    count += 1

print(count)
print(F(count))
print(time() - start)