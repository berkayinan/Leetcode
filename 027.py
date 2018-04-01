class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow,fast=0,0
        while fast<len(nums):
            while fast<len(nums) and nums[fast]==val:
                fast+=1
            if fast==len(nums):
                break
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
        return slow