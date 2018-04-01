class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows==1:
            return s
        result=[]
        period = numRows*2 - 2
        for r in range(numRows):
            for i in range(r,len(s),period):
                result.append(s[i])
                if r!=0 and r!=numRows-1 and i+period-2*r<len(s):
                    result.append(s[i+period-2*r])
        return ''.join(result)
        