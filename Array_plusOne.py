#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        digits[-1] = 1
        digits.append(-1)
        return plusOne(digits)

#print(plusOne([1,2,3,4]))
print(plusOne([9,9]))