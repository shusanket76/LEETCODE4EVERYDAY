class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkpalindrome(l, r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if checkpalindrome(l, r-1) is True:
                    return True
                elif checkpalindrome(l+1, r) is True:
                    return True
                return False
        return True