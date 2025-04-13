class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range (0,len(nums)):
            if target - nums[i] in my_dict:
                return (i,my_dict[target - nums[i]])
            else:
                my_dict[nums[i]]= i

            