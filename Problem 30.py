from timeit import default_timer as time

start = time()
ListOfNumbers = []
for i in range(2,354294):
    SumOfDigitsPowered = 0
    for count in str(i):
        SumOfDigitsPowered += int(count)**5
    if SumOfDigitsPowered == i:
        ListOfNumbers.append(i)
print(sum(ListOfNumbers))
print(time()-start)
