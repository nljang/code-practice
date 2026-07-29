class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_of_each_num = defaultdict(int)

        for n in nums:
            count_of_each_num[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in count_of_each_num.items():
            buckets[freq].append(num)
        
        answer = []

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer


