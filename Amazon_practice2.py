from operator import indexOf


giftMatrix = ['1100', '1110', '0110', '0001']
#giftMatrix = ['11000', '11100', '01100', '00001', '00011']


def gift(g):
    if len(g) == 1:
        return 1
    else:
        g = ['']
        for i in range(len(giftMatrix)):
            j = i+1
            if giftMatrix[i][j] == '1':
                print(i, j)
                g.append(str(i) + str(j))
                j -= 1
            else:
                j += 1
            if len(giftMatrix) == j:
                break
    print(g)


gift(giftMatrix)

'''
def gift(g):
    if len(g) == 1:
        return 1
    else:
        g = ['']
        for i in range(len(giftMatrix)):
            j = len(giftMatrix)-i-1
            if giftMatrix[i][i+1] == '1':
                print(i, j)
                g.append(str(i) + str(j))
                j+=1
            else:
                j-=1
    print(g)


gift(giftMatrix)
'''
###############################
# Attempt 3 -- ? ms
###############################
'''
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

mydict = dict.fromkeys(mylist)
print(mydict)
'''
