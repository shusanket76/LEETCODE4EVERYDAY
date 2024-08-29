class Solution:
    def findLongestChain(self, pairs):
        currend = float("-inf")
        pairs.sort(key = lambda x : x[1])
        l = 0
        # print(pairs)
        res = []
        while l<len(pairs):
            if pairs[l][0]>currend:
                currend = pairs[l][1]
                res.append(pairs[l])
            l+=1
        return len(res)
        # ToDo: Write Your Code Here.
        # return 0  # Return the maximum chain length

