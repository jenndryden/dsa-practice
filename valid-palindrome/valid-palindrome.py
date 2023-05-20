class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        r = len(s) - 1
        l = 0

        while r > l:
            if not self.isAlphaNumeric(s[l]) and r > l:
                l += 1
                continue
            if not self.isAlphaNumeric(s[r]) and r > l:
                r -= 1
                continue

            if s[r].lower() != s[l].lower():
                return False
            
            r -= 1
            l += 1
        return True
    
    def isAlphaNumeric(self, c):
        if ((ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))):
            return True
        return False