class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        for n in range(len(candies)):
            if extraCandies + candies[n] >= maxi:
                candies[n] = True
            else:
                candies[n] = False
        return candies

print(Solution.kidsWithCandies(Solution, [2,3,5,1,3], 3))