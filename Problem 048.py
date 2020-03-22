from timeit import default_timer as time

start = time()
print(str(sum([x**x for x in range(1,1000+1)])))
print(time()-start)