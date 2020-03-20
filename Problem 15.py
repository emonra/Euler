from math import factorial as factorial

#This is just a math problem
#In a 20x20 grid, you must go sideways 20 times and down 20 times for a total of 40 times
#The solution is just to choose when to go down, which is 40C20

answer = factorial(40)/(factorial(20) * factorial(20))

print(answer)