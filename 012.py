class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters=[('','M'),('D','C'),('L','X'),('V','I')]
        res=[]
        for _ in range(num//1000):
            res.append('M')
        num-=(num//1000)*1000
        base=100
        base_level=1
        while base>0:
            digit=num//base
            if digit==4:
                res.append(letters[base_level][1])
                res.append(letters[base_level][0])
            elif digit==9:
                res.append(letters[base_level][1])
                res.append(letters[base_level-1][1])
            else:
                if digit>=5:
                    res.append(letters[base_level][0])
                    digit-=5
                for _ in range(digit):
                    res.append(letters[base_level][1])
            num-=(num//base)*base
            base_level+=1
            base//=10
        return ''.join(res)



        
        