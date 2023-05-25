from collections import Counter
s, t = "car", "rat"
k, l = "kale", "lake"
q, x = "anagram", "nagaram"

###############################
# Attempt 3 -- 18 ms
###############################


def validAnagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return


print(validAnagram("cart", "rat"))
print(validAnagram(s, t))
print(validAnagram(k, l))
print(validAnagram(q, x))

###############################
# Attempt 4 -- 34 ms
###############################


def isAnagram(a, b):
    print("Counter(a)", Counter(a), "Counter(b)", Counter(b), "type:", type(Counter(a)))
    return Counter(a) == Counter(b)


print(isAnagram("cart", "rat"))
print(isAnagram(s, t))
print(isAnagram(k, l))
print(isAnagram(q, x))

###############################
# Attempt 2 - DOESNT WORK
###############################
'''
def validAnagram(a,b):
    d1, d2 = {}, {}
    if len(a) != len(b):
        return
    elif a is b:
        return True
    
    for v in a:
        if v not in b:
            return
        else:
            d1[v] +=1
'''
###############################
# Attempt 1 - DOESNT WORK
###############################
'''
def validAnagram(a, b):
    r = []

    if len(a) != len(b):
        return
    for i in range(len(b)):
        if b[i] in a:
            r[i] = b[i+1:]
        else:
            return
    return
'''
