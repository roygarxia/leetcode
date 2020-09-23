#Two Number Sum!

def twoNumSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            return [array[left], array[right]]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    return []


print(twoNumSum([10,40,30,20,10,48,48,20], 40))


