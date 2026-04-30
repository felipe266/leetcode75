class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            maior = str1
            menor = str2
        else:
            maior = str2
            menor = str1
        
        mdc = 1
        nmaior = len(maior)
        nmenor = len(menor)
        i = 2
        if nmaior % nmenor == 0:
            mdc = nmenor
        else:
            while i <= nmenor:
                if nmaior%i == 0 and nmenor%i == 0:
                    mdc *= i
                    nmaior = nmaior//i
                    nmenor = nmenor//i
                    i = 2
                i+=1
        t = menor[:mdc]
        s = ""
        while len(s) < len(maior):
            s += t
            if len(s) == len(menor):
                if s != menor:
                    return ""
            if len(s) == len(maior):
                if s != maior:
                    return ""
        return t

print(Solution.gcdOfStrings(Solution,"RGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJ", "RGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJRGOAQOBGJ"))
#NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM
# str1,str2 = "ABABAB", "ABAB"
# str2 = str2[:len(str2)-len(str1)%len(str2)]
# print(len(str1)%len(str2))
# print(str2)