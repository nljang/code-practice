from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for word in strs:
            freq_map = [0] * 26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            
            anagram[tuple(freq_map)].append(word)
        
        return list(anagram.values())