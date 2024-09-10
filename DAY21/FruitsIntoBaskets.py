class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hasmap = {}
        l = 0
        haset = set()
        r = 0
        res = 0
        while r<len(fruits):
            haset.add(fruits[r])
            if fruits[r] in hasmap:
                hasmap[fruits[r]]+=1
            else:
                hasmap[fruits[r]]=1
            while l<len(fruits) and len(haset)>2:
                hasmap[fruits[l]]-=1
                if hasmap[fruits[l]]==0:
                    haset.remove(fruits[l])
                l+=1
            res = max(res, r-l+1)
            r+=1
        return (res)
            