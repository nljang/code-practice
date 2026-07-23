from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #inputs: array of strings
        #output: list of lists of anagrams [['cat', 'tac'], ['rat', 'tar']]

        answer = []
        seen = defaultdict(list) #{key = freq map: value is list of original words}
        for word in strs:
            #initialize its own freq map
            freq_map = [0] * 26
            for char in word:
                freq_map[ord(char) - ord('a')] += 1
            #check if freq map been seen before (means an anagram)
            seen[tuple(freq_map)].append(word)

        for word in seen.values():
            answer.append(word)
        return answer


        #strs = ["act","pots","tops","cat","stop","hat"]

        #seen: {act: [act, cat], pots: [pots, tops, stop], hat: [hat]}
        #output = [[act, cat], [pots, tops, stop], [hat]]