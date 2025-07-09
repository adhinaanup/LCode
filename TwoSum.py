class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)
        
        new=[]
        for i in range(l):
            c=nums[i]
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    new.append(i)
                    new.append(j)

        return new
                
        
