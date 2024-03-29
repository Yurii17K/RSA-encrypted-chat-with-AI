def isBigger(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1IsNegative = isEqual(num1[0], '-')
    num2IsNegative = isEqual(num2[0], '-')

    if (num1IsNegative and not num2IsNegative):
        return False
    elif (not num1IsNegative and num2IsNegative): 
        return True
    elif (num1IsNegative and num2IsNegative):
        return not isBigger(num1[1:], num2[1:])
    
    if (len(num1) > len(num2)):
        return True
    if (len(num1) < len(num2)):
        return False
    for x in range(len(num1)):
            if(num1[x] > num2[x]):
                return True
            elif (isEqual(num1[x], num2[x])):
                continue
            else: return False
    return False

def isBiggerOrEqual(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    return not isSmaller(num1, num2)

def isSmaller(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1IsNegative = isEqual(num1[0], '-')
    num2IsNegative = isEqual(num2[0], '-')
    
    if (num1IsNegative and not num2IsNegative):
        return True
    elif (not num1IsNegative and num2IsNegative): 
        return False
    elif (num1IsNegative and num2IsNegative):
        return isBigger(num1[1:], num2[1:]) 
    else: 
        if (len(num1) < len(num2)):
            return True
        if (len(num1) > len(num2)):
            return False
        for x in range(len(num1)):
                if(num1[x] < num2[x]):
                    return True
                elif (isEqual(num1[x], num2[x])):
                    continue
                else: return False
        return False

def isEqual(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if(not len(num1) == len(num2)):
        return False
    for x in range(len(num1)):
           if (not num1[x] == num2[x]):
                return False
    return True
            

def sumLT(number1, number2):
    sumLookupTable = {
        -9: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],
        -8: [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1],
        -7: [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2],
        -6: [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3],
        -5: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],
        -4: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        -3: [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
        -2: [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7],
        -1: [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
        0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        3: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        4: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        5: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        6: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        7: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        8: [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        9: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        10: [10, 11],
        11: [11, 12],
        12: [12, 13],
        13: [13, 14],
        14: [14, 15],
        15: [15, 16],
        16: [16, 17],
        17: [17, 18],
        18: [18, 19]
    }
    return sumLookupTable[number1][number2]

def diffLTNoNegatives(num1, num2):
    if (num2 == 0):
        return num1
    diffTable = {
        0: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        1: [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        2: [1, 0, 9, 8, 7, 6, 5, 4, 3, 2],
        3: [2, 1, 0, 9, 8, 7, 6, 5, 4, 3],
        4: [3, 2, 1, 0, 9, 8, 7, 6, 5, 4],
        5: [4, 3, 2, 1, 0, 9, 8, 7, 6, 5],
        6: [5, 4, 3, 2, 1, 0, 9, 8, 7, 6],
        7: [6, 5, 4, 3, 2, 1, 0, 9, 8, 7],
        8: [7, 6, 5, 4, 3, 2, 1, 0, 9, 8],
        9: [8, 7, 6, 5, 4, 3, 2, 1, 0, 9],
        10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        11: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        12: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
        13: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
        14: [13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
        15: [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
        16: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        17: [16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
        18: [17, 16, 15, 14, 13, 12, 11, 10, 9, 8],
        19: [18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
    }
    return diffTable[num1][num2 - 1]
    

def diffLT(number1, number2):
    if (isEqual(number2, 0)):
        return number1
    diffTable = {
        -10: [-11, -12, -13, -14, -15, -16, -17, -18, -19, -20], 
        -9: [-10, -11, -12, -13, -14, -15, -16, -17, -18, -19], 
        -8: [-9, -10, -11, -12, -13, -14, -15, -16, -17, -18], 
        -7: [-8, -9, -10, -11, -12, -13, -14, -15, -16, -17], 
        -6: [-7, -8, -9, -10, -11, -12, -13, -14, -15, -16], 
        -5: [-6, -7, -8, -9, -10, -11, -12, -13, -14, -15], 
        -4: [-5, -6, -7, -8, -9, -10, -11, -12, -13, -14], 
        -3: [-4, -5, -6, -7, -8, -9, -10, -11, -12, -13], 
        -2: [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12], 
        -1: [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11], 
        0: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],
        1: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9],
        2: [1, 0, -1, -2, -3, -4, -5, -6, -7, -8],
        3: [2, 1, 0, -1, -2, -3, -4, -5, -6, -7],
        4: [3, 2, 1, 0, -1, -2, -3, -4, -5, -6],
        5: [4, 3, 2, 1, 0, -1, -2, -3, -4, -5],
        6: [5, 4, 3, 2, 1, 0, -1, -2, -3, -4],
        7: [6, 5, 4, 3, 2, 1, 0, -1, -2, -3],
        8: [7, 6, 5, 4, 3, 2, 1, 0, -1, -2],
        9: [8, 7, 6, 5, 4, 3, 2, 1, 0, -1],
        10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        11: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        12: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
        13: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
        14: [13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
        15: [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
        16: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        17: [16, 15, 14, 13, 12, 11, 10, 9, 8, 7],
        18: [17, 16, 15, 14, 13, 12, 11, 10, 9, 8],
        19: [18, 17, 16, 15, 14, 13, 12, 11, 10, 9],
    }
    return diffTable[number1][number2 - 1]