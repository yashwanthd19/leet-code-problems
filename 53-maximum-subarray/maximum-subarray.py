class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0]
        m=nums[0]
        for n in nums[1:]:
            c=max(n,c+n)
            m=max(m,c)
        return m