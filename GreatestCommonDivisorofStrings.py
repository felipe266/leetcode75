class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1) > len(str2)):
            maior = str1
            menor = str2
        else:
            maior = str2
            menor = str1
        
        if maior%menor == 0:
            temp = ""
            quant = len(maior)//len(menor)
            for _ in range(quant):
                temp += maior