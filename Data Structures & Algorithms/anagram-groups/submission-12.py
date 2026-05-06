class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            freq_map = [0] * 26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            if tuple(freq_map) in seen:
                seen[tuple(freq_map)].append(word)
            else:
                seen[tuple(freq_map)] = [word]
        
        return list(seen.values())
