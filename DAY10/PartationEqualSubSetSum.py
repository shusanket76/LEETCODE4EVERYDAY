class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for x in nums:
            total+=x
        if total%2!=0:
            return False
        target = total//2
        hasmap = {}
        def dfs(pointer, target):
            if target == 0:
                return True
            if (pointer, target) in hasmap:
                return False
            if pointer>=len(nums) or target<0:
                return False
            a = dfs(pointer+1, target-nums[pointer])
            if a is True:
                return True
            b = dfs(pointer+1, target)
            if b is True:
                return True
            hasmap[(pointer, target)]=False
            return False
        return dfs(0, target)
            
        


        dfs(pointer, target)
        