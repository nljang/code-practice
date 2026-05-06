class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_map, t_freq_map = {}, {}

        for char in s:
            if char in s_freq_map:
                s_freq_map[char] += 1
            else:
                s_freq_map[char] = 1
        
        for char in t:
            if char in t_freq_map:
                t_freq_map[char] += 1
            else:
                t_freq_map[char] = 1
        
        return s_freq_map == t_freq_map
