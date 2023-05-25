nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxsub(nums):

    if len(nums) <= 2:
        return sum(nums)
    rs, max = 0, 0
    for i in range(0, len(nums)):
        rs += nums[i]
        if rs > 0:
            max += nums[i]
            print("max:", max)
            #rs = max
        else: rs = 0
        print(rs)
    return max


print("total:", maxsub(nums))
print("total:", maxsub([5, 4, -1, 7, 8]))
