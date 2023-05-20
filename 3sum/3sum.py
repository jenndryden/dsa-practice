class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for first in range(len(nums)):
            second = first + 1
            last = len(nums) - 1
            if first > 0 and nums[first] == nums[first-1]:
                continue
            while second < last:
                if nums[first] + nums[second] + nums[last] > 0:
                    last -= 1
                elif nums[first] + nums[second] + nums[last] < 0:
                    second += 1
                else:
                    result.append([nums[first], nums[second], nums[last]])
                    while second < last and nums[second] == nums[second + 1]:  # skip same number
                        second += 1
                    while second < last and nums[last] == nums[last - 1]:  # skip same number
                        last -= 1
                    second += 1
                    last -= 1
        return result