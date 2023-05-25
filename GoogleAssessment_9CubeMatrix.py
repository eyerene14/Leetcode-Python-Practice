
def matrixN(n):

    if n <= 1:
        #print("n:", n)
        return n+n
    else:
        print("n:", n, "n-1*2", (n-1)*n)
        return matrixN(n-1)+matrixN(n-2)+matrixN(n-2)


print(matrixN(3))  # print(matrixN((input("Enter n rows: "))))
