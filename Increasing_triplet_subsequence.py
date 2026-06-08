class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tam = len(nums)
        first = max(nums)
        second = max(nums)
        for n in range(tam):
            if(first >= nums[n]):
                first = nums[n]
            elif second >= nums[n]:
                second = nums[n]
            else:
                return True
        return False

S = Solution.increasingTriplet(Solution,[20,100,10,9,5,13])
print(S)