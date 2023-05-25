numbers = [2,7,11,15]
target = 9

def twoSums(nums, t):
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    
    for i in range(len(nums)):
        

print(twoSums(numbers,target))