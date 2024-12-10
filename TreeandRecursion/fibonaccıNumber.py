def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+ fibonacci(num-2)

print(fibonacci(10))

"""
class Solution(object):
    def fib(self, n):
        # Base cases
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case
        return self.fib(n - 1) + self.fib(n - 2)

# Example usage
solution = Solution()
print(solution.fib(10))  # Output: 55

"""
def iterativeFib(n):
    x,y=0,1
    for i in range(n):
        x,y=y,x+y #bir öncekini birbiri ile toplar. aynı çözüm.
    return x

print(iterativeFib(10))

#memoization
#daha önceden hesapladığımız durumların tekrar tekrar üzerinden geçilmesi gerekirse bir yere kaydetme mantığıdır.
#timeit kütüphanesi loopu tekrar tekrar çalıştırıp zaman ölçer cpu yorar maksat time hesaplamak.
#Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

#Iterative
class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1

        for i in range(n):
            x,y = y,x+y

        return x

#Memoization - we should include a list of fib number calculations to see the effect
class Solution:
    def fib(self, n: int) -> int:
        def iterativeSolution(n):
            x,y = 0,1
            for i in range(n):
                x,y = y,x+y
            return x
        
        memo = {}

        if n not in memo:
            memo[n] = iterativeSolution(n)

        return memo[n]  