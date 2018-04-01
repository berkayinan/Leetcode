class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainder={}
        for i,n in enumerate(nums):
            if target-n in remainder:
                return [remainder[target-n],i]
            remainder[n]=i            
        