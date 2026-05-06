from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        seen_words = defaultdict(list)
        for word in strs:
            freq_sig = [0] * 26
            for char in word:
                freq_sig[ord(char) - ord('a')] += 1
            seen_words[tuple(freq_sig)].append(word)
        
        return list(seen_words.values())
            

