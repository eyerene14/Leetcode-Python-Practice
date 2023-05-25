#nums = [1, 4, 4, 2, 1, 3, 1, 5]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

###############################
# Attempt 1 -- ? ms
###############################
def returnUniqueCount(nums):
    count = 0

    for i in range(1, len(nums)):
        if nums[i-1] ^ nums[i] == 0:
            count += 1
        print(nums[i-1] ^ nums[i])
    return count


print("count: ", returnUniqueCount(nums))

###############################
# Attempt 2 -- ? ms
###############################
def returnUniqueValuesArray(nums):
    k = []
    j = 1

    for i in range(0, len(nums)):
        if nums[i] != nums[j]:
            k.append(nums[i])
            j = i
        else: j += 1
    return k


print(returnUniqueValuesArray(nums))

###############################
# Attempt 3 -- ? ms
###############################
mylist = ["a", "b", "a", "c", "c"]
mydict = dict.fromkeys(mylist)
print(mydict)
mylist = list(dict.fromkeys(mylist))
print(mylist)
