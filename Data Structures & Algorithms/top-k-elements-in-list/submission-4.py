from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        answer = []
        
        for freq in range(len(buckets) -1, 0, -1):  #len bc bucekts is a list of lists and range needs an int
            for num in buckets[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer
