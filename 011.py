class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start,end = 0, len(height)-1
        best = 0
        while start<end:
            best=max(best,min(height[end],height[start])*(end-start))
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return best
        