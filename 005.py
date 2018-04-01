class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best_idx=0,0
        dyn=[[False for _ in s] for _ in s]
        # 1-length
        for i in range(len(s)):
            dyn[i][i]=True
        # 2-length
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dyn[i][i+1]=True
                best_idx=(i,i+1)
        # >2-length
        for l in range(2,len(s)):
            for i in range(len(s)-l):
                if s[i]==s[i+l]:
                    dyn[i][i+l] = dyn[i+1][i+l-1]
                    if dyn[i][i+l]:
                        best_idx=(i,i+l)
        return s[best_idx[0]:best_idx[1]+1]
        