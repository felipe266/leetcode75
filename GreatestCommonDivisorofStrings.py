class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            maior = str1
            menor = str2
        else:
            maior = str2
            menor = str1
            
        while len(maior)%len(menor) != 0:
            menor = menor[:len(menor)-len(maior)%len(menor)]
        tem = 1
        for n in range(1,len(menor)):
            if menor[n] == menor[n]:
                tem += 1
        if tem == len(menor):
            return ""
        temp = ""
        for n in range(0,len(maior),len(menor)):
            if(maior[n:len(menor)+n] == menor):
                temp += menor
        if temp == maior:
            return menor
        else:
            return ""

print(Solution.gcdOfStrings(Solution,"AAAAAAAAA", "AAACCC"))

# str1,str2 = "ABABAB", "ABAB"
# str2 = str2[:len(str2)-len(str1)%len(str2)]
# print(len(str1)%len(str2))
# print(str2)