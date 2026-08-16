class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count0=0
        count1=0
        count2=0
        for s in stones:
            r=s%3
            if r==0:
                count0+=1
            elif r==1:
                count1+=1
            else:
                count2+=1
        if count0%2==0:
            return count1>0 and count2>0
        else:
            return abs(count1-count2)>2 
        