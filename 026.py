class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast=0,0
        while fast<len(nums):
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
            while fast<len(nums) and nums[fast]==nums[fast-1]:
                fast+=1
        return slow
            