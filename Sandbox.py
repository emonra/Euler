from timeit import default_timer as time

start = time()

list_of_multiples = [x for x in range(1,1000) if (x%3==0 or x%5==0)]
sum2 = sum(list_of_multiples)
print(sum2)
print(time()-start)