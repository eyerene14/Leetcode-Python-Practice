### primes 1-100: 
### 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,
### 107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,181,191,193,197,199
####################
# ATTEMPT 3: count primes between 3:n - 34ms
####################
def countPrimes1(n):
    if n <= 2:
        return 0
    primes = {2}

    for i in range(3,n):
        is_div = False
        for p in primes:
            if i%p == 0:
                is_div = True
        if not is_div:
            primes.add(i)
            
    return len(primes)



def countPrimes(n):
    if n <= 2:
        return 0

    def checkP(p, n): 
        sqr = int(n ** .5)
        for i in range(2,sqr):
            if p % i != 0:
                return p

    primes = {2}
    for i in range(3,n):
        primes.add(checkP(i, n))
    return primes

    

print(countPrimes(10))

####################
# ATTEMPT 2: count primes between 3:n - 23ms
####################
def primesCount(n):
    if n < 2:
        return 0
    else:
        nonPrimes = set()
        p = 2
        while p * p < n:
            for i in range(p * 2, n + 1, p):
                nonPrimes.add(i)
            p += 1

    count = 0
    for v in range(2,n,1):
        if v not in nonPrimes:
            count +=1
    return count

print(primesCount(10))

####################
# ATTEMPT 1: this is a function call - ?ms
####################
def checkPrimality(n):
    sqr = int(n ** .5)

    for i in range(2, sqr+1):
        if n % i != 0:
            print(i)


checkPrimality(10)
