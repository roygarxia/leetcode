#from collections import defaultdict
def singleNumber(nums) -> int:
        hash_table = dict()
        for i in range(len(nums)):
            hash_table[nums[i]] = 0
        
        for i in range(len(nums)):
            hash_table[nums[i]] += 1
            
        for i in hash_table:
            if hash_table[i] == 1:
                return i


print(singleNumber([49,495,38,184,588,388,388,588,184,495,49]))