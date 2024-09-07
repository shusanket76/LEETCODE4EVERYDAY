class Solution:
    def maxSubArrayLen(self, nums, k):
        # ToDo: Write Your Code Here.
        hasmap = {}
        temp = 0
        res = 0
        for x in range(len(nums)):
            temp+=nums[x]
            wehave = temp-k
            if wehave in hasmap:
                # print(hasmap[wehave], (x+1))
                val = (x+1) - hasmap[wehave]
                res = max(res, val)
                print(res)
            if temp == k:
                res = max(res, x+1)
            hasmap[temp] = x+1
        
        return res  

