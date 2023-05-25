# Calculating the Time complexity
#best, others = big_o.big_o(function, collection ,n_measures=len(collection))
# print(best)

x1 = 123
x2 = -123
x3 = 120

r1 = 0
r2 = 0
r3 = 0


def flipInt(x):
    r = ''
    while x:
        if x % 10 > 0:
            r += str(x % 10)
        x = x // 10
    print(r)


# flipInt(x1)
flipInt(x3)
flipInt(x2)


def flipInt2(x):
    newX = ''
    for v in reversed(str(x)):
        if v != '0':
            newX += v
    return newX

# print(flipInt2(x3)) ## 33ms
