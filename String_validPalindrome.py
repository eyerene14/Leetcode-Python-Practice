import collections
from curses.ascii import isalpha
from collections import Counter

s = "A man, a plan, a canal: Panama"


def validPalindrome(s):

    def removeNonAlpha(str):
        alphaS = ''
        for char in str.lower():
            if char.isalpha():
                alphaS += char
        return alphaS

    alphaS = removeNonAlpha(s)

    for first in range(0, len(alphaS)//2):
        last = len(alphaS) - first - 1
        if alphaS[first] != alphaS[last]:
            print(alphaS[first], alphaS[last])
            return False
    return True


print(validPalindrome(s))
