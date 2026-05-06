class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        hashIndex = 0
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = True
        return False