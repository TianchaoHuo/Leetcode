
'''Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not 
    use the same element twice.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
     Because nums[0] + nums[1] = 2 + 7 = 9,
     return [0, 1].'''
     
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
		    
# Using the  Hash Table 		    
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Hash = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            other=target-nums[i]
            if Hash.get(other) and Hash[other] != i :
                return [i,Hash[other]]
        # there is a bug for [1,3,4,2] taget :6  ------->nums[ Hash[other]]!=nums[ i] 
        # 
        # also for [3, 3] target :6     -------------> Hash[other] != i 
	
	'''The better  performance code'''
class Solution(object):
   	 def twoSum(self, nums, target):
        		d={}
        		for i,num in enumerate(nums):
           	 if target-num in d:
               		 return d[target-num], i
            	d[num]=i
			
	