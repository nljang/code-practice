from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countBRUH = defaultdict(int)

        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countBRUH[n] += 1
        
        for n, c in countBRUH.items():
            buckets[c].append(n)   #NOT buckets[c] = n bc that will replace value if already there
        
        answer = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answer.append(num)
            if len(answer) == k:
                return answer