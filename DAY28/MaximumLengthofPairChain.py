class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        res = [pairs[0]]
        r = 1
        while r<len(pairs):
            lastele = res[-1]
            currele = pairs[r]
            if lastele[1]<currele[0]:
                res.append(pairs[r])
            r+=1
        return len(res)
        