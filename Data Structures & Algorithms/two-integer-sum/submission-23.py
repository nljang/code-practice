class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need], key]
            else:
                seen[value] = key