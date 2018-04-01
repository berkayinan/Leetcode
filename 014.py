class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        
        if len(strs)==0:
            return ""
        res=[]
        minLen = min([len(s) for s in strs])
        for i in range(minLen):
            c = strs[0][i]
            for s in strs:
                if s[i]!=c:
                    return ''.join(res)
            res.append(c)
        return ''.join(res)