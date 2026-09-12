class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = [0] * 26
        t_chars = [0] * 26

        for char in s:
            s_chars[ord(char) - ord('a')] += 1

        for char in t:
            t_chars[ord(char) - ord('a')] += 1

        return s_chars == t_chars