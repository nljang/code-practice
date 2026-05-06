from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  #if a word not in dictionary default to list so dont get keyerror

        for word in strs:
            count = [0] * 26 #for each word make 26 boxes, one for each letter

            for char in word:                #for each character in each word, 
                count[ord(char) - ord('a')] += 1      #take ascii value to find what letter and map to the count list

            result[tuple(count)].append(word) #tuple it cuz cant use list as key in python dicts

        return list(result.values())



