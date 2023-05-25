nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDups():
    nums1 = nums[:]
    for n in nums1:
        if n in nums1:
            nums1.remove(n)
    return nums1

print(removeDups())

#the for loop doesn't have enough values and errors at end
def deleteDups():
    nums2 = nums[:]
    for i in range(len(nums2)):
        if nums2[i] in nums2:
            del(nums2[i])
    print(nums2)

deleteDups()

