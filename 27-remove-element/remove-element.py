class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        a=0
        for b in range(len(nums)):
            if nums[b]!=val:
                nums[a]=nums[b]
                a=a+1
        return a