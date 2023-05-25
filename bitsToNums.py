##############################
## This reads the bits from left to right e.g. 10 -> 0b1010 if bit = 1: i1=1 i2=0; i3=1; i4=0;
##############################
def bitsToNumber(bits):
    num = 0

    for bit in bits:
        num = num << 1
        
        if bit == '1':
            num+=1
    return num

print(bitsToNumber('1001')) # output --> 12
print(bitsToNumber('1100')) # output --> 12
print(bitsToNumber('10010')) # output --> 18
print(bitsToNumber('1010')) # output --> 10

def numbersToBits(n):
    bits = ''
    while n:
        #print(str(n & 1))
        bits = str(n & 1) + bits 
        n >>= 1
    print(bits)

numbersToBits(9)
numbersToBits(5)