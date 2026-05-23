class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tam = len(flowerbed)
        quant = posb = 0
        for m in flowerbed:
            if m == 1:
                quant+=1
        if tam%2 == 0:
            posb = tam/2
        else:
            posb = (tam+1)/2
        if quant + n > posb:   
            return False
        i = 0
        step = 1
        while n > 0 and i < tam:
            print(i)
            if flowerbed[i] == 0:
                if i == tam -1:
                    flowerbed[i] = 1
                    n-=1
                    break
                if flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n-=1
                else:
                    step = 1
            else:
                step = 2
            i+= step
        print(flowerbed)
        if n == 0:
            return True
        else:
            return False
            



S = Solution.canPlaceFlowers(Solution,[0,1,0,0,1,0,0], 1)

print(S)