def fib(n): # returns nth fibo number
    fibs = [0] * max(n+1,2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]

    return fibs[6]

print(fib(100000))