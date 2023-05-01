def arithm_progression(a1: float, d: float, n: int) -> list:
    """ an = a1 + (n-1) * d"""
    # result = []
    # for i in range(n):
    #     result.append(a1+i*d)
    # return result
    return [a1+i*d for i in range(n)]


a1 = float(input("Enter the first element of arithmetic progression A1: "))
d = float(input("Enter the delta of arithmetic progression D: "))
n = int(input("Enter the number of elements of arithmetic progression N: "))

print(arithm_progression(a1, d, n))
