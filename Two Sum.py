class Solution(object):
    def twoSum(self, nums, target):
        num_map={}
        for i,num in enumerate(nums):
            c=target-num
            if c in num_map:
                return [num_map[c],i]
            num_map[num]=i
        
