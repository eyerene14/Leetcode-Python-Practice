''' OPTION 1
nums = [1, 4, 4, 2, 1, 1, 3, 5]
stringList = ["one", "two", "three"]

for word in reversed(stringList):
    print(word)


def iterReverse():
    k = len(nums) - 1

    for i in range(k, -1, -1):
        print("index:", i, "value:", nums[i])

iterReverse()

'''

#####################################
# 17ms
#####################################
hello = ["h", "e", "l", "l", "o"]


def reverseString(s):
    newS = []

    for v in reversed(s):
        newS.append(v)
    return newS


print(reverseString(hello))

#####################################
# 8ms
#####################################
s = ["H", "a", "n", "n", "a", "h"]

s.reverse()
print(s)

#####################################
# 22ms
#####################################
t = ["H", "a", "r", "r", "y"]

for i in range(len(t)):
    t.insert(i, t.pop())
print(t)

#####################################
# 22ms
#####################################
b = ["b", "u", "g", "g", "y"]

for i in range(len(b)//2):
    j = len(b) - i - 1
    temp = b[i]
    b[i] = b[j]
    b[j] = temp

print(b)
