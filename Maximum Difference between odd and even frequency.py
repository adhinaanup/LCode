class Solution(object):
    def maxDifference(self, s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        odd=[]
        even=[]
        for count in freq.values():
            if count%2==0:
                even.append(count)
            else:
                odd.append(count)
        maxi=-float('inf')
        for a1 in odd:
            for a2 in even:
                maxi=max(maxi,a1-a2)
        return maxi
        
