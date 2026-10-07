class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed=''
        for char in s:
            if char.isalnum():
                trimmed+=char.lower()
        return trimmed==trimmed[::-1]

        