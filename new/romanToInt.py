class Solution(object):
    def romanToInt(self, s):
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        prev=0
        for i in reversed(s):
            value=val[i]
            if value<prev:
                total-=value
            else:
                total+=value
                prev=value
        return total


        
