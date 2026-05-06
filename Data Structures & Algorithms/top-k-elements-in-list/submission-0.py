from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] += 1       #frequency map of how many times
        
        for n, c in hashmap.items():   # for (number, # of count) same as enumerate for lists but instead of index and value since this is dictionary it gives key, value
            buckets[c].append(n)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1): #goes backwards from highest to 0 in steps of -1
            for n in buckets[i]:          #for every num in current highest frequency:
                result.append(n)          #add to result list
                if len(result) == k:      #until we get to len(k)
                    return result
