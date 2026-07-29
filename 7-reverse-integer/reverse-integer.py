class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if(x<0):
            neg=True
        x=abs(x)
        rev=0
        while x>0:
            digit=x%10
            rev=(rev*10)+digit
            x=x//10
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        if(neg):
            rev=-rev
        return rev
        