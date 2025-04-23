class Solution(object):
    def productExceptSelf(self, nums):
        product ,zero_count = reduce(lambda a,b:a*(b if b else 1),nums,1),nums.count(0)
        if zero_count>1:
            return [0]*len(nums)
        for i, value in enumerate(nums):
            if zero_count:
                nums[i]=0 if value else product
            else:
                nums[i]=product // value
        return nums               
        
                
