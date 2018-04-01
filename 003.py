class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window
        start, end = 0,0
        idx={}
        best_len = 0
        while end<len(s):
            # Check if it is a duplicate
            if s[end] in idx:
                dup_index=idx[s[end]]
                while start<=dup_index:
                    idx.pop(s[start])
                    start+=1
            best_len = max(best_len,end-start+1)
            idx[s[end]]=end
            end+=1
        return best_len