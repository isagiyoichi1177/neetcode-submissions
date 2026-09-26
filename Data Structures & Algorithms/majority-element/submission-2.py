class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        for num in count:
            if count[num]>n//2:
                return num        