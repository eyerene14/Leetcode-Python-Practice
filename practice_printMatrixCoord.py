'''from collections import Counter
n = 3'''

"""
def printMatrix(n):

    for i in range(0, n):
        print("row:", i, end="")
        for j in range(i, n):
            print(" ", j, end="")
        print()


# printMatrix(3)

def printMatrix2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, end="")
            print(j, end=" ")
        print()

"""
# printMatrix2(3)

giftMatrix = ['1100', '1110', '0110', '0001']
# for j in range(len(i)):
"""
for i in giftMatrix:
    for j in range(1, len(i)):
        #print(int(i[j-1]) | int(i[j]), end="")
    #print()
"""
'''
d1 = {}

for i in range(len(giftMatrix)):
    for j in giftMatrix[i]:
        d1[j] = int(j) + i
        print(i, end="")
        print(j, end=" ")
    print(d1)
'''

group = []


def printRow(n=3, d={1: 1, 2: 2}):
    print(d)
    if n in d:
        return [n]
    else:
        rsum = printRow(n-1, d) + printRow(n-2, d)
        d[n] = rsum
        return rsum


def printColumn(rowL, n):

    for i in range(len(rowL)):
        rowL[i] += n
    return rowL


print(printRow(3))
group = printRow(3)
# print(group)
