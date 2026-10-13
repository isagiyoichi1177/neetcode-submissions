class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frq={}
        n=len(nums)
        result=[]
        for num in nums:
            if num in frq:
                frq[num]+=1
            else:
                frq[num]=1

        for num in frq:
            if frq[num]>n/3:
                result.append(num)

        return result