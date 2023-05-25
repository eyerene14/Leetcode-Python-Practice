
nums = [2, 2, 1]


def getSingle(nums):
    uniqueN = 0
    for v in nums:
        uniqueN ^= v
    return uniqueN


print(getSingle(nums), 'unique in %s' % nums)

nums = [2, 2, 1, 1, 6]
print(getSingle(nums), 'unique in %s' % nums)

nums = [4, 1, 2, 1, 2]
print(getSingle(nums), 'unique in %s' % nums)

nums = [1]
# print(getSingle(nums))

#nums = [4, 1, 2, 1, 2]
# a ^ b compares each digit in a vs b.
# if digit is == then digit in same position = 0 else 1
# iteration: num vs nums[i]
# 0: num = 0 vs 100
# 1: num = 4 vs 1 = 5 -- 100 vs 1 = 101
# 2: num = 5 vs 2 = 7 -- 101 vs 10 = 111
# 3: num = 7 vs 1 = 6 -- 111 vs 1 = 110
# 4: num = 6 vs 2 = 4 -- 110 vs 10 = 100
