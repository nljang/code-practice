class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [nums.index(diff), index]
            else:
                hashmap[num] = index