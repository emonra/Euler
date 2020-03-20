from timeit import default_timer as time
from  num2words import  num2words

start = time()
def wordNumber(number):
    letterNumbers=[]
    for j in range(1,number):
        toWordNumber=num2words(j)
        letterNumbers+=[toWordNumber]
    for g in range(len(letterNumbers)):
        car=''
        for j in range(len(letterNumbers[g])):
            if letterNumbers[g][j]!=' ' and letterNumbers[g][j]!='-' :
                car+=letterNumbers[g][j]
        letterNumbers[g]=car
    return letterNumbers 
listNumber=wordNumber(1001)

def counting(a):
    Sum=0
    for j in range(len(a)):
        Sum+=len(a[j])
    return Sum

print(counting(listNumber))
print(time() - start)