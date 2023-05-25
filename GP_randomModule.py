import random
from audioop import avg

import random
total = [1, 2, 3, 4, 5, 6, 7, 8, 9] #length = 8

print("row sum:", sum(total))

random3 = random.sample(total, 3)
print("random3:", random3)

for i in range(0,3,1):
    print("random.randint():", random.randint(0,11))

'''
randInt = random.randint(1, 10)
print(randInt)
choice = random.choice(total)
print(choice)

print(random.shuffle(total))
print(total)
'''