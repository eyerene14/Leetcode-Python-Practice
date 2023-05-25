nums = [0,1,0,3,12]

def moveZeros(l):
    l2 = []

    while 0 in l:
        l.remove(0)
        l2.append(0)
    return l + l2

print(moveZeros(nums))

print(moveZeros([0]))