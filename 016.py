class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        best_total=sum(nums[:3])
        nums.sort()
        for i in range(len(nums)):
            start,end = i+1,len(nums)-1
            while start<end:
                total=nums[start]+nums[end]+nums[i]
                if abs(target-best_total)>=abs(target-total):
                    best_total=total
                if target>total:
                    start+=1
                elif target<total:
                    end-=1
                else:
                    return best_total
        return best_total
                    
        