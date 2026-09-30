class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a=0
        for b in range(1,len(nums)):
            if nums[a]!=nums[b]:
                a=a+1
                nums[a]=nums[b]
    
        return a+1
        