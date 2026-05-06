class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setted_nums = set(nums)
        if len(setted_nums) != len(nums):
            return True
        return False