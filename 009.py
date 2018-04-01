class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        res=0
        cur=x
        while cur:
            res=res*10+cur%10
            cur//=10
        return res==x
        
        
            
        