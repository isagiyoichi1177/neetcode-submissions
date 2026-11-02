class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stored_nums=sorted(set(nums))
        if not stored_nums:
            return 0
        ls=1
        cs=1
        prenums=stored_nums[0]
        for index in range(1,len(stored_nums)):
            if stored_nums[index]==prenums+1:
                cs+=1
            else:
                cs=1
            prenums = stored_nums[index]
            ls=max(ls,cs)
        return ls
        
        


