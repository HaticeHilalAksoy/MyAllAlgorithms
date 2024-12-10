'''
fonksiyonun içinde aynı fonksiyonun tekrar çağrılmasına denir.
'''

def calculateFactorial(num):
    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num - 1)
calculateFactorial(5)
calculateFactorial(6)

def calculateContigousSum(num):
    
    if num == 0:
        return 0
    else:
        return num + calculateContigousSum(num - 1)
calculateContigousSum(3)
calculateContigousSum(4)
calculateContigousSum(6)

myList = [5,10,15,5,20,15,5,10,5,100,10,20,15,100,5,10]
def fibIterative(n: int) -> int:
    x,y = 0,1
    for i in range(n):
        x,y = y,x+y
    return x
# %%timeit -r 1000 -n 1000
for num in myList:
    fibIterative(num)

# %%timeit -r 1000 -n 1000
def fib(n: int) -> int:
    x,y = 0,1
    for i in range(n):
        x,y = y,x+y
    return x  
    
memo = {}

def memoizationSolution(n):
    if n not in memo:
        memo[n] = fib(n)
    return memo[n]

myList = [5,10,15,5,20,15,5,10,5,100,10,20,15,100,5,10]

for num in myList:
    memoizationSolution(num)
