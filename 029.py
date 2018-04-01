class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):
            if i>0 and nums[i-1]<nums[i]:
                j=len(nums)-1
                while nums[j]<=nums[i-1]:
                    j-=1
                nums[j],nums[i-1]=nums[i-1],nums[j]
                start,end=i,len(nums)-1
                while start<end:
                    nums[start],nums[end]=nums[end],nums[start]
                    start+=1
                    end-=1
                return
        nums.sort()