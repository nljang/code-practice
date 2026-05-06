class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        hashmap = {}
        startNums = []
        consecutives = []

        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for num in nums:
            if num - 1 in hashmap:
                pass
            else:
                startNums.append(num)

        def check(num, answer):
            if num + 1 not in hashmap:
                return answer
            else:
                return check(num + 1, answer + 1)

        for num in startNums:
            answer = check(num, 0)
            consecutives.append(answer)
        
        if len(consecutives) == 0:
            print('what')
        else:
            return max(consecutives) + 1

            

