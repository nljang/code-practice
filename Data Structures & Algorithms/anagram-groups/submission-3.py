from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            frequency_signature = [0] * 26
            for char in word:
                frequency_signature[ord(char) - ord('a')] += 1
        
            results[tuple(frequency_signature)].append(word)

        return list(results.values())