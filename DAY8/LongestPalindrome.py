class Solution:
    def longestPalindrome(self, s: str) -> int:
        hasmap = {}
        oddfound = False
        for x in s:
            if x in hasmap:
                hasmap[x]+=1
            else:
                hasmap[x]=1
        minodd = 0
        res = 0
        for a,b in hasmap.items():
            if b%2==0:
                res+=b
            else:
                oddfound =True
                res+=(b-1)
        if oddfound:
            res+=1
        return res
        