class Solution:

    def encode(self, strs: List[str]) -> str:
        done = ''
        for word in strs:
            done = done + str(len(word))
            done = done + '#'
            done = done + word
        return done

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i < len(s):     #while i isnt at the end of the encoded string:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # the length of the word is from pointer i to pointer j
            answer.append(s[j + 1 : j + 1 + length])  # append what comes +1 after '#' aka start of new word to end of new word
            i = j + 1 + length
        return answer

