class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        result_set=[]
        letters={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def permutate(index,result,result_set):
            if index==len(digits):
                result_set.append(''.join(result))
                return
            for letter in letters[digits[index]]:
                result[index]=letter
                permutate(index+1,result,result_set)
                
        permutate(0,['' for _ in digits],result_set)
        return result_set
        