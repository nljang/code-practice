from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_map, t_freq_map = defaultdict(int), defaultdict(int)

        for char in s:
            s_freq_map[char] += 1
        
        for char in t:
            t_freq_map[char] += 1
        
        return s_freq_map == t_freq_map
