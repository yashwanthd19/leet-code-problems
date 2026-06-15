class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        def canBreak(a, b):
            for i in range(len(a)):
                if a[i] < b[i]:
                    return False
            return True
        return canBreak(s1,s2) or canBreak(s2,s1)