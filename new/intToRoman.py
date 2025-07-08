class Solution(object):
    def romanToInt(self, s):
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman=""
        for i in range(len(val)):
            while s>=val[i]:
                roman+=sym[i]
                s -= val[i]
        return roman


        
