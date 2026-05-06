class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                if hashmap[diff] < index:
                    return [hashmap[diff], index]
                else:
                    return [index, hashmap[diff]]
            hashmap[value] = index 
        