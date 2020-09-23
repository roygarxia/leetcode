def threeNumberSum(array, targetSum):
    # Write your code here.
	assert(len(array) > 2) #if you have less than 3 values in the array, there is no 3 sum
    array.sort() #sorting an array sometimes helps
	triplets = [] #initialize the returned array
	
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			testSum = array[i] + array[left] + array[right]
			if testSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif testSum < targetSum:
				left += 1
			elif testSum > targetSum:
				right -= 1
			
	return triplets