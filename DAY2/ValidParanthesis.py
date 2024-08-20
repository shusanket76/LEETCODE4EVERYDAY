class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hasmap = {"(":")", "{":"}", "[":"]"}
        for x in s:
            if x in hasmap:
                res.append(x)
            else:
                if len(res)!=0:
                    if hasmap[res[-1]]==x:
                        res.pop()
                    else:
                        return False
                else:
                    return False
        return len(res)==0
                

        self.start