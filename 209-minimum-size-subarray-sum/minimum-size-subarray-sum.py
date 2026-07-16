class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left=0
        curr_sum=0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                mini=min(mini,right-left+1)
                curr_sum-=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0
        