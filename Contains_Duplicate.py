class Solution(object):
    def containsDuplicate(self, nums):
        has = {}
        for num in nums:
            if num not in has:
                has[num]=1
            else:
                return True
        return False   