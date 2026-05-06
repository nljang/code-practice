from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for word in strs:
            freq_signature = [0] * 26
            for char in word:
                freq_signature[ord(char) - ord('a')] += 1
            answer[tuple(freq_signature)].append(word)

        return list(answer.values())
