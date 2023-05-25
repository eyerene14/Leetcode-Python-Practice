matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotateImage(m):
    for i in range(len(m)):
        temp = m[i]
        m[i] = left[i]