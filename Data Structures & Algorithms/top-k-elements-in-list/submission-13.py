class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for num in seen:
            buckets[seen[num]].append(num)

        answer = []
        for bucket in reversed(buckets):
            for num in bucket:
                answer.append(num)
                if len(answer) == k:
                    return answer

