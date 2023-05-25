word = "leetcode"

def firstUniqChar(w):
    d = {}
    for k in w:
        if k not in d:
            d[k] = 1
        else:
            d[k] += 1

    '''for key, value in d.items():
        print(key, "value:", value)
    '''
    for v in w:
        if d[v] == 1:
            return w.index(v)
    return -1
    
#print(firstUniqChar(word)) #--> expected output: 0
print(firstUniqChar("loveleetcode")) #--> expected output: 2
print(firstUniqChar("aabb")) #--> expected output: -1