class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        l = ""
        for n in range(len(words)-1,-1,-1):
            l += words[n]
            if n != 0:
                l += " "
        return l

S = Solution.reverseWords(Solution, "abc der fgh ")
print(S)