nums = [2,7,11,15]
target = 9

def twoSums(l, t):
    l2 = []

    for i in range(len(l)):
        if t == l[i]:
            return [i]
