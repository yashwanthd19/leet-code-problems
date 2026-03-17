class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=max(nums)
        nums.sort()
        c=0
        for i in range(n+1):
            if(i == nums[i]):
                c+=1
            else:
                break
        return c

        
        