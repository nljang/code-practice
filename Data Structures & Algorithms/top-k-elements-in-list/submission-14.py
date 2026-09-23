class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range((len(nums) + 1))]

        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        for n in seen:
            buckets[seen[n]].append(n)
        
        answer = []
        for bucket in reversed(buckets):
            for n in bucket:
                answer.append(n)
                if len(answer) == k:
                    return answer

            