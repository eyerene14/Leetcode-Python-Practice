###############################
# Attempt 1 -- 16 ms
###############################
def findNeedle(a,b):

    if b in a:
        return b.find(a)
    else:
        return 0

haystack, needle = "hello", "ll"
print(findNeedle(haystack, needle))
#index expected - output = 2