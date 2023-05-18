class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given nums and traget
        # return indices of two numbers that add up to target
            seen = {}
            for i, number in enumerate(nums):
                if target - number in seen:
                    return [seen[target - number], i]
                seen[number] = i
            return [] 