
def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        if len(nums) == 1:
            return False
        
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                return True
        return False

print(containsDuplicate([1,2,3,1]))