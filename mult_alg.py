from sum_alg import sumAlg
from diff_alg import diffAlg
from utils_alg import *

def multAlgB10(num1, num2):
    return multAlg(num1, num2, 10)

def multAlg(num1, num2, base):
    longerNum = str(num1)
    shorterNum = str(num2)
    res = ""
    carry = 0
    negative = False

    if (isSmaller(len(longerNum), len(shorterNum))):
        tmpSwap = longerNum
        longerNum = shorterNum
        shorterNum = tmpSwap

    if(isEqual(longerNum[0], '-') and isEqual(shorterNum[0], '-')):
        raise Exception("Developer has a mistake somewhere, there cant be negative numbers over FF")
        longerNum = longerNum[1:]
        shorterNum = shorterNum[1:]
    elif(isEqual(longerNum[0], '-') and not isEqual(shorterNum[0], '-')):
        raise Exception("Developer has a mistake somewhere, there cant be negative numbers over FF")
        negative = True
        longerNum = longerNum[1:]
    elif(not isEqual(longerNum[0], '-') and isEqual(shorterNum[0], '-')):
        raise Exception("Developer has a mistake somewhere, there cant be negative numbers over FF")
        negative = True
        shorterNum = shorterNum[1:]

    longerNumLen = len(longerNum)
    shorterNumLen = len(shorterNum)

    for lowerRowI in range(shorterNumLen):
        tmpRowMult = ""
        for upperRowI in range(longerNumLen):
            tmpMult = 0

            # perform 'multiplication' by adding the lowerNum upperNum-times to itself
            for y in range(int(longerNum[diffAlg(diffAlg(longerNumLen, upperRowI, base=10, prime=None), 1, base=10, prime=None)])):
                tmpMult = sumAlg(tmpMult, shorterNum[diffAlg(diffAlg(shorterNumLen, lowerRowI, base=10, prime=None), 1, base=10, prime=None)], base)

            tmpMult = sumAlg(tmpMult, carry, base) # add carry

            baseDivisions = 0
            if (not isEqual(upperRowI, longerNumLen - 1)):
                # perform 'division' by base to get the result and a carry
                while (isBiggerOrEqual(tmpMult, base)):
                    tmpMult = diffAlg(tmpMult, base, base, None)
                    baseDivisions = sumAlg(baseDivisions, 1, base)
                carry = baseDivisions
            else: carry = 0 # do not divide for last (first in written form) number of the upper row, just 'bring' it down

            tmpRowMult += str(tmpMult)[::-1]

        res = sumAlg(res, int(tmpRowMult[::-1] + ('0' * lowerRowI)), base)

    if not negative:
        return res
    else: 
        raise Exception("""Developer has a mistake somewhere, there cant be negative numbers over FF. 
         This error is deep and should have not been reached""")
        return int('-' + str(res))


# print(multAlg(61231212335647, 3467347357134, 10))