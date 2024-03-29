from div_alg import divAlgB10
from utils_alg import *
from utils import *
from add_points_EC import add_points

# Formulas are taken from https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_doubling
# Formulas are taken from https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition

def fast_addition(A:int, p:int, P, n:int):
    m = n
    if isEqual(n, 0):
        return None, None
    if isEqual(n, 1):
        return P

    DOUBLES = P
    ODD = (None, None)
    multiplicationsDone = 1

    # double log2(n) times
    while isBiggerOrEqual(n, 2):
        DOUBLES = add_points(A, p, DOUBLES, DOUBLES)
        n = divAlgB10(n, 2)[0]
        multiplicationsDone = multAlgB10(multiplicationsDone, 2)

    # recursive call to speed up the reminders instead of a loop of additions
    # (i dont want 31 calls for addition when lets say n is 63 and etc)
    ODD = fast_addition(A, p, P, diffAlgB10(m, multiplicationsDone, None))

    return add_points(A, p, DOUBLES, ODD)

# TESTS
# print(fast_addition(33, 71, (15, 44), 35))
# print(fast_addition(33, 45, 71, (8, 53), 1))
# print(fast_addition(6, 31, (6, 14), 4))
# P = (15, 44)
# X = P
# for x in range(2, 100):
#     print(fast_addition(33, 71, P, x),  x)
# for x in range(2, 50):  
#     X = add_points(33, 71, X, P)
#     print(X, x)
# print(add_points(33, 71, (56, 36), (56, 36)))
