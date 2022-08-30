def fib(n):  # returns nth fibo number
    fibs = [0] * max(n + 1, 2)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]


# print(fib(10))

import numpy as np


def grid_traveler(n, m):  # (rows, columns)
    # grid = [[0 for _ in range(n)] for _ in range(m)]
    grid = np.zeros(shape=(n + 1, m + 1), dtype=np.longdouble)
    grid[1, 1] = 1

    for r in range(n + 1):
        for c in range(m + 1):
            try:
                grid[r + 1, c] += grid[r, c]
            except IndexError:
                pass
            try:
                grid[r, c + 1] += grid[r, c]
            except IndexError:
                pass

    print(grid)
    return grid[-1, -1]


# print(grid_traveler(5, 5))

def canSum(targetSum, numbers: list):  # numbers in the list are reuseable
    table = [False] * (targetSum + 1)
    table[0] = True

    for i in range(targetSum + 1):
        if table[i]:  # if true
            for num in numbers:
                try:
                    table[i + num] = True
                except IndexError:
                    pass
    return table[-1]


# print(canSum(21, [11,13,17,23]))
# print(canSum(300, [7,14]))

def howSum(targetSum, numbers: list):  # numbers in the list are reuseable
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:  # if it is list type
            for num in numbers:
                try:
                    if table[i + num] is None:  # Some non empty list exists there
                        table[i + num] = [*table[i], num]
                except IndexError:
                    pass

    # print(table)
    return table[-1]


# print(howSum(6, [1,2,3,4]))
# print(howSum(30, [2,3,5,6,10]))
# print(howSum(50, [2,3,4,6,7]))
# print(howSum(127, [11,13,17,23]))
# print(howSum(127, [23,17,13,11]))
# print(howSum(300, [7,14]))
# print(howSum(8, [2,3,5]))


def bestSum(targetSum, numbers: list):  # numbers in the list are reuseable
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:  # if it is list type
            for num in numbers:
                try:
                    if len(table[i + num]) > len(table[i]):  # Choose the shorter option
                        table[i + num] = [*table[i], num]
                except TypeError:  # in case of type error, do the default thing
                    table[i + num] = [*table[i], num]
                except IndexError:
                    pass

    # print(table)
    return table[-1]


# print("BEST SUM BELOW---------")
# print(bestSum(6, [1,2,3,4]))
# print(bestSum(30, [2,3,5,6,10]))
# print(bestSum(50, [2,3,4,6,7]))
# print(bestSum(127, [11,13,17,23]))
# print(bestSum(127, [23,17,13,11]))
# print(bestSum(300, [7,14]))
# print(bestSum(8, [2,3,5]))


#
# def can_construct(target:str, WordBank:list) -> bool:
#     # table = np.zeros(shape=(len(target)+1,len(WordBank)+1), dtype=np.longdouble)
#     # table = np.array([[False for i in range(len(WordBank)+1)] for j in range(len(target)+1)])
#     tb = [['' for i in range(len(WordBank) + 1)] for j in range(len(target) + 1)]
#     # table[0,0] = True # If target is empty string, then It can be created
#     for row in range(len(target)+1):
#         for col in range(len(WordBank) + 1):
#             try:
#                 tb[row][col+1] += WordBank[col]
#                 tb[row+1][col] += WordBank[col]
#             except IndexError:
#                 pass
#
#     print(tb)
#
# can_construct('boyisgood', ['boy', 'is', 'good'])

def can_construct(target: str, WordBank: list) -> bool:
    tb = [False] * (len(target) + 1)
    tb[0] = True

    for i in range(0, len(target) + 1):
        for word in WordBank:
            try:
                if tb[i]:
                    if target[i:].startswith(word):
                        tb[i + len(word)] = True
            except IndexError:
                pass
    return tb[-1]


print("<----CAN CONSTRUCT---->")
print(can_construct('boyisgood', ['boy', 'is', 'good']))
print(can_construct('', ['boy', 'is', 'good']))
print(can_construct('boyisgood', ['boy', 'i', 'is', 'good']))
print(can_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'er']))
print(can_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'e']))


def count_construct(target: str, WordBank: list) -> int:
    tb = [0] * (len(target) + 1)
    tb[0] = 1

    for i in range(0, len(target) + 1):
        for word in WordBank:
            try:
                if tb[i]:
                    if target[i:].startswith(word):
                        tb[i + len(word)] += tb[i]
            except IndexError:
                pass
    return tb[-1]


print("<----COUNT CONSTRUCT---->")

print(count_construct('boyisgood', ['boy', 'is', 'boyis', 'good', 'go', 'od']))
print(count_construct('', ['boy', 'is', 'good']))
print(count_construct('boyisgood', ['boy', 'i', 'is', 'good']))
print(count_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'er']))
print(count_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'e']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
    'eeeeee',
    'ef',
    'f',
    'eef',
    'eeef',
    'eeeef'
]))


def all_construct(target: str, WordBank: list):
    # tb = [[0]] * (len(target)+1)
    tb = [[] for _ in range(len(target) + 1)]
    tb[0] = [[]]

    for i in range(0, len(target) + 1):
        for word in WordBank:
            try:
                if target[i:].startswith(word):
                    # if not tb[i+len(word)]:
                    c1 = list(map(lambda x: [*x, word], tb[i]))
                    tb[i + len(word)] += (c1)
                    # else:
                    #     c = list(map(lambda x: [*x, word], tb[i]))
                    #     tb[i + len(word)].append(*c)
                    #     # c = list(map(lambda way: [way, word],tb[i+len(word)]))
                    # tb[i+len(word)] = c
            except IndexError:
                pass
    # print(tb)
    return tb[-1]


print("<----ALL CONSTRUCT---->")
#
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('boyisgood', ['boy', 'is', 'boyis', 'good', 'go', 'od']))
print(all_construct('', ['boy', 'is', 'good']))
print(all_construct('boyisgood', ['boy', 'is', 'good']))
print(all_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'er']))
print(all_construct('calmerboy', ['boy', 'i', 'is', 'good', 'calm', 'e']))
# print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeee',
#     'eeeee',
#     'eeeeee',
#     'eeeeee',
#     'ef',
#     'f',
#     'eef',
#     'eeef',
#     'eeeef'
# ]))
