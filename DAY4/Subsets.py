class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(pointer, curr):
            if pointer>=len(nums):
                res.append(curr[:])
                return
            curr.append(nums[pointer])
            dfs(pointer+1, curr)
            curr.pop()
            dfs(pointer+1, curr)
        dfs( 0, [])
        return res
        