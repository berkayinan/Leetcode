class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        comp={')':'(',
              ']':'[',
              '}':'{'}
        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if len(stack)==0 or stack.pop()!=comp[c]:
                    return False
        return len(stack)==0
        