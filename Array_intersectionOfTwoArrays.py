nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

#print({*nums1} & {*nums2})
#print("{*nums1}", {*nums1})
#print("{*nums2}", {*nums2})

nums3 = [9, 4, 9, 8, 4]
nums4 = [4, 9, 5]

print(list({*nums3} | {*nums4}))
#print("{*nums3}", {*nums3})
#print("{*nums4}", {*nums4})


def intersection(num1, num2):
    res = list()
    nums1 = list(set(num1))
    for i in range(len(nums1)):
        if nums1[i] in num2:
            res.append(nums1[i])
    return res


print(intersection(nums1, nums2))
print(intersection(nums3, nums4))
