# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/
# Recursion Practice

def getRow(rowIndex):
    if rowIndex == 1:
        print("n1:", rowIndex)
        return 1
    else:
        print("n:", rowIndex)
        # print(rowIndex, "(", rowIndex-1, ",", rowIndex-2, ")")
        return [getRow(rowIndex-2)] + [getRow(rowIndex-2)*rowIndex] + [getRow(rowIndex-2)*rowIndex] + [getRow(rowIndex-2)]
        # return [getRow(rowIndex-2)] + [getRow(rowIndex-2)*rowIndex]*rowIndex + [getRow(rowIndex-2)]


print(getRow(3))
