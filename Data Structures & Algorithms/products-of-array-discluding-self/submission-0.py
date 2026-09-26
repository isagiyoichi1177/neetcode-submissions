class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        reslut=[1]*n
        prefix=1
        for i in range(n):
            reslut[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            reslut[i]*=suffix
            suffix *=nums[i]
        return reslut
