from queue import deque

nums = [1,2,3,4,5]
q1 = deque(nums) 
q = deque()

q.append(1) #--> adds value to the right (end of array)
q.appendleft(2) #--> adds value to the left at index 0 (beginning of array) and existing pushes values right
q.append(3) #--> adds value to the right (end of array)
print(q)
q.popleft() #--> removes value at index 0 (beginning of array)
print(q) 
q1Popped = q1.popleft()
print(q1)
#print(q1Popped)

while len(q1): #stops when len() = 0 in codeblock
    print(len(q1))
    q1.popleft()
    print("postpopped left:", len(q1))