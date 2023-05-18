class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_list = set(nums)
        if len(new_list) != len(nums):
            return True
        else:
            return False 