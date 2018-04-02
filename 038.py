class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev=["1"]
        for _ in range(1,n):
            cur=0
            new_result=[]
            while cur<len(prev):
                count=1
                cur+=1
                while cur<len(prev) and prev[cur]==prev[cur-1]:
                    cur+=1
                    count+=1
                new_result.append(str(count))
                new_result.append(prev[cur-1])
            prev=new_result
        return ''.join(prev)