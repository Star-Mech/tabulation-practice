def fib(n): # returns nth fibo number
    fibs = [0] * max(n+1,2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]

    return fibs[n]

# print(fib(10))

import numpy as np
print(np.__version__)

def grid_traveler(n,m): # (rows, columns)
    # grid = [[0 for _ in range(n)] for _ in range(m)]
    grid = np.zeros(shape=(n+1,m+1), dtype=np.longdouble)
    grid[1,1] = 1

    for r in range(n+1):
        for c in range(m+1):
            try:
                grid[r+1,c] += grid[r,c]
            except IndexError:
                pass
            try:
                grid[r,c+1] += grid[r,c]
            except IndexError:
                pass

    print(grid)
    return grid[-1,-1]
print(grid_traveler(5,5))