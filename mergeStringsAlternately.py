class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sum = word1 + word2
        temp = ''
        for n in range(len(sum)):
            if(n < len(word1)):
                temp += word1[n]
            if(n<len(word2)):
                temp += word2[n]
        return temp

print(Solution.mergeAlternately(Solution, "ab", "pqrs"))