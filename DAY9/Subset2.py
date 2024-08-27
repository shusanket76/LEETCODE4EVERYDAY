class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, curr, pointer):
            if pointer>=len(nums):
                res.append(curr[:])
                return 
            curr.append(nums[pointer])
            dfs(nums,curr, pointer+1)
            curr.pop()
            while pointer<len(nums)-1 and nums[pointer]==nums[pointer+1]:
                pointer+=1
            dfs(nums, curr, pointer+1)
        
        dfs(nums, curr=[], pointer=0)
        return (res)
        