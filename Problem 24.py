from itertools import permutations as perm
from timeit import default_timer as time
start = time()
print (''.join(list(perm('0123456789',10))[999999]))
print(time()-start)