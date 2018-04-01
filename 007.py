class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_lim = 2**31-1
        isNegative=False
        if x<0: 
            x*=-1
            isNegative=True
        result=0
        while x:
            result=result*10+x%10
            x//=10
        if result>int_lim:
            return 0
        if isNegative:
            result*=-1
        
        return result