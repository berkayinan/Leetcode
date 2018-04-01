class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        cur=0
        sign=1
        while str[cur]==' ':
            cur+=1
        if str[cur]=='-':
            sign=-1
            cur+=1
        elif str[cur]=='+':
            cur+=1
        result=0
        for c in str[cur:]:
            if ord('0')>ord(c) or ord('9')<ord(c):
                break
            result*=10
            result+=ord(c)-ord('0')
        result*=sign
        result = min(2**31-1,result)
        result = max(-(2**31),result)
        return result
        
        
        