# 9/22/2020
'''
    In this LC problem we must restore a string given an array of integers that may or may not be out
    of order. The shuffled string must follow the sorted array.
    Example:
        input: "DCBA", [3, 2, 1, 0]
        output: "ABCD"
'''


def restoreString(str, array):
    shuff_str = ''
    for i in range(len(array)):
        shuff_str += str[array.index(i)]

    print(shuff_str)
    return shuff_str

restoreString("DCBA", [3, 2, 1, 0])
restoreString("KCID", [3, 2, 1, 0])
restoreString("YOR", [2,1,0])
