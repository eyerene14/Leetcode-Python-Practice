#~~~ MIT Lecture 6: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lec6_recursion_dictionaries/
#~~~ MIT code: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/706228e592761d9c7c1c073f8ba7a6cc_lec6_recursion_dictionaries.py

def fastFib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

print(fastFib(4))

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 34
#print("")
#print('using fib')
#print(fib(argToUse))
#print("")
#print('using fib_efficient')
#print(fib_efficient(argToUse, d))

def fib_iteration(n):
    f = [1,1]
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
    return f[n]

print(fib_iteration(5))