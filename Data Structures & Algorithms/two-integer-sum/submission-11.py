class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                if index < nums.index(diff):
                    return [index, nums.index(diff)]
                return [nums.index(diff), index]
            else:
                seen[value] = index
