from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []

        seen_freqs = defaultdict(list)
        
        for word in strs:
            freq_map = [0] * 26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            seen_freqs[tuple(freq_map)].append(word)
        
        for x in seen_freqs.values():
            answer.append(x)
        
        return answer