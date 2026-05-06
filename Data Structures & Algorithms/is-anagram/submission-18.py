class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_map = [0] * 26
        t_freq_map = [0] * 26

        for char in s:
            s_freq_map[ord(char) - ord('a')] += 1
        
        for char in t:
            t_freq_map[ord(char) - ord('a')] += 1
        
        return s_freq_map == t_freq_map
