class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dictionary = {}
        
        for i, num1 in enumerate(nums):
            num2 = target - num1
            
            if num2 in num_dictionary:
                return[num_dictionary[num2], i]
            num_dictionary[num1] = i
            
        return []
    
twosum = Solution()
result = twosum.twoSum([2,7,11,15], 18)
print(result)