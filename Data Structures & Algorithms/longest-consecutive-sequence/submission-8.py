class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set()
        for n in nums:
            seen.add(n)
        
        max_answer = 1
        for n in nums:
            if (n - 1) not in seen:
                answer = 1
                curr = n
                while (curr + 1) in seen:
                    answer += 1
                    curr += 1
                max_answer = max(max_answer, answer)
                
        
        return max_answer
                


