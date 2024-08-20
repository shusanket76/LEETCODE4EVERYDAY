class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hasm = {}
        res = float("inf") 
        for x in text:
            if x in hasm:
                hasm[x]+=1
            else:
                hasm[x]=1
        # balloon
        if "b" in hasm and "a" in hasm and "l" in hasm and "o" in hasm and "n" in hasm:
            res = min(res, hasm["b"])
            res = min(res, hasm["a"])
            res = min(res, hasm["n"])
            res = min(res, hasm["l"]//2)
            res = min(res, hasm["o"]//2)
        if res==float("inf"):
            return 0
        return res
        
        

