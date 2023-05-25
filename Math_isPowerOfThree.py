# powers of three = 0,3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969
####################
# ATTEMPT 2: is n a power of 3 - 23ms
####################
def isPowerOfThree(n):
    if n == 0:
        return False

    x = 0
    while 3**x <= n:
        print(3**x)
        if (3**x) == n:
            return True
        x += 1
    return False
    
n = int(input("Enter a guess for power of 3: "))
print(isPowerOfThree(n))

####################
# ATTEMPT 1: is n a power of 3 - 31ms
####################
def isPowerOfThree1(n):
    if n == 0:
        return False
        
    primeCheck = any(3**x == n for x in range(0,n))
        
    return primeCheck
