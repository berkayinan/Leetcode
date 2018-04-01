class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sols=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start,end = i+1,len(nums)-1
            while start<end:
                total=nums[start]+nums[end]
                if total>-nums[i]:
                    end-=1
                elif total<-nums[i]:
                    start+=1
                else:
                    sols.append((nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
                    while nums[start]==nums[start-1] and start<end:
                        start+=1
                    while nums[end]==nums[end+1] and start<end:
                        end-=1
                        
        return sols