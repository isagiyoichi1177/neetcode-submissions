class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        un=[]
        for num in nums:
            if num not in seen:
                seen.add(num)
                un.append(num)
        nums[:]=un
        return len(un)