class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=sorted(nums)
        n=len(nums)
        print(a)
        return a[n-k]
        