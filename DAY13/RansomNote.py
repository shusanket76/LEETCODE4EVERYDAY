from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ToDo: Write Your Code Here.
        hasmap = {}
        for x in magazine:
            if x in hasmap:
                hasmap[x]+=1
            else:
                hasmap[x]=1
        for y in ransomNote:
            if y in hasmap and hasmap[y]!=0:
                hasmap[y]-=1
            else:
                return False
        return True
