class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        a=sorted(nums)
        for i in range(len(nums)-1):
            c=max(a[i],a[i+1])
            b=min(a[i],a[i+1])
            a[i]=c-b
        a[-1]=0
        print(a)
        return max(a)