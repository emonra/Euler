from timeit import default_timer as time

start = time()
DT = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        DT.append(c)
DT = list(set(DT))
print(len(DT))
print(time()-start)