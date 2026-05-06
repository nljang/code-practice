class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums = set(nums)
        if len(newNums) == len(nums):
            return False
        return True