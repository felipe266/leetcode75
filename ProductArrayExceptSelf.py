class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tam = len(nums)
        prefixo = [1]*tam
        for n in range(1,tam):
            prefixo[n] = prefixo[n-1] * nums[n-1]
        
        sufixo = [1]*tam
        for n in range(tam-2,-1,-1):
            sufixo[n] = sufixo[n+1]*nums[n+1]
        
        answer = [1]*tam
        for n in range(tam):
            answer[n] = prefixo[n]*sufixo[n]
        
        return answer


S = Solution.productExceptSelf(Solution, [-1,1,0,-3,3])
print(S)