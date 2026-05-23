class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vowelsin =[]
        frase = []
        vowelsposi = [0]*(len(s))
        for n in range(len(s)):
            if s[n].lower() in vowels:
                vowelsin.append(s[n])
                vowelsposi[n] = 1
            frase.append(s[n])

        tam = len(vowelsin)
        f = ""
        for m in range(len(s)):
            if vowelsposi[m] == 1:
                frase[m] = vowelsin[tam-1]
                tam -= 1
            f += frase[m]
        return f

s  = Solution.reverseVowels(Solution, "leetcode")

print(s)
