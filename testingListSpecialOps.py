from multiprocessing.sharedctypes import Value


nums = [1, 2, 3, 1, 0]


def testingAny(num):

    return (any(num))


print(testingAny(nums))


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


node = Node('help', 'me')

print(dir(node))

for i, v in enumerate(nums):
    print(i, v)
