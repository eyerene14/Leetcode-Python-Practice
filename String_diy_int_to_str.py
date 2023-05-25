###############################
# Attempt 1 -- ? ms
###############################
def getIntFromString(line):
    o = '0123456789'
    r = ''

    for char in line:
        if char == '-':
            r+= char
        elif char in o:
            r += o[int(char)]
    if r > 2 ** 31-1 | r < -2 ** 31:
        return 0
    return r

#print(getIntFromString("42"))
# 42

print(getIntFromString("   -42"))
# -42

#print(getIntFromString("4193 with words"))
# 4193
