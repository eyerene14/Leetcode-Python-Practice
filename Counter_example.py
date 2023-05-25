from collections import Counter

mylist = ["a", "b", "a", "c", "c"]
intlist = [1,2,3,1,2]
letterCount= Counter(mylist)
intCount= Counter(mylist)
print(Counter(mylist))
print(Counter(intlist))
print(letterCount.get('a'))