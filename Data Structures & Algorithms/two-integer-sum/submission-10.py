class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                if nums.index(diff) < i:
                    return [nums.index(diff),i]
                return [i,nums.index(diff)]
            else:
                hashmap[j] = i
