class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a=0
        for b in range(len(nums)):
            if a<2 or nums[b]!=nums[a-2]:
                nums[a]=nums[b]
                a=a+1
        return a
        