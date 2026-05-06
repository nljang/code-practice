from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            freqmap = [0] * 26
            for char in word:
                freqmap[(ord(char) - ord('a'))] += 1
            seen[tuple(freqmap)].append(word)

        
        return list(seen.values())