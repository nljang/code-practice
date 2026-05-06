class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        hashset = set()
        start_nums = []
        consecutives = []

        for n in nums:
            hashset.add(n)
        
        for n in nums:
            if n - 1 in hashset:
                pass
            else:
                start_nums.append(n)
        
        def check(n, answer):
            if n + 1 not in hashset:
                return answer
            else:
                return check(n + 1, answer + 1)

        for n in start_nums:
            answer = check(n, 1)
            consecutives.append(answer)
        
        return max(consecutives)
