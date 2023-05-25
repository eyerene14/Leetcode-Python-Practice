from queue import deque

num = [1, 2, 3, 4, 5, 6, 7]

def rotateArray(array, k):
    q = deque()
    n = len(num) - 1
    for i in range(n-k, -k, -1):
        print(i)
        q.appendleft(num[i])
    return q


print(rotateArray(num, 3))
print(rotateArray(num, 5))
