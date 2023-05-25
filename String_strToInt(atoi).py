
def atoi(s):
    num= ""

    if s[-1].isdigit():
        return 0
    for v in s.strip():
        if not v.isalpha():
            num += v

    if int(num) < -2**31:
        return -2**31
    elif int(num) > (2**31)-1:
        return (2**31)-1

    return int(num)
    
print(atoi("4193 with words"))
print(atoi("   -42"))