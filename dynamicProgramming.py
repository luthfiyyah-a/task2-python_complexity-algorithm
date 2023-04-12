counterPlainRecursive = 0
counterDynamicProgramming = 0

def fibonacciPlainRecursive(n):
    global counterPlainRecursive
    counterPlainRecursive += 1
    if n<2:
        return n
    return fibonacciPlainRecursive(n-1) + fibonacciPlainRecursive(n-2)


def fibonacciDynamicProgramming():
    cache = {}
    def fib(n):
        nonlocal cache
        # nonlocal counterDynamicProgramming
        global counterDynamicProgramming
        counterDynamicProgramming += 1
        if n in cache:
            return cache[n]
        elif n<2:
            return n
        else:
            cache[n] = fib(n-1) + fib(n-2)
            return n
    return fib
            

fibonacciPlainRecursive(20)
fasterFibonacci = fibonacciDynamicProgramming()
fasterFibonacci(20)
print('we did ' + str(counterPlainRecursive) + ' calculations for Plain Recursive')
print('we did ' + str(counterDynamicProgramming) + ' calculations for Dynamic Programming')