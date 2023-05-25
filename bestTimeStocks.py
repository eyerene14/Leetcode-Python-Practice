prices = [7, 1, 5, 3, 6, 4]
prices1 = [7, 6, 4, 3, 1]
# prices2 = [1,2,3,4,5]


def stockProfit(nums):
    profit = 0
    p = 0
    j = 0

    for i in range(len(nums)):
        if nums[j] < nums[i]:
            p = nums[i] - nums[j]
            profit += p
            print("j", j, "p", p, profit)
        else:
            j = i - 1
        j += 1
    return profit


print("prices:", end=" ")
print(stockProfit(prices))
# print("prices1", stockProfit(prices1))
# print("prices2", str(stockProfit(prices2)))
