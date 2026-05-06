class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for s_char in s:
            s_list.append(s_char)
        for t_char in t:
            t_list.append(t_char)
        
        if sorted(s_list) == sorted(t_list):
            return True
        else:
            return False



        
        