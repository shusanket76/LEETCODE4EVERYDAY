class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums):
            if len(nums)==1:
                return [nums[:]]
            perm = []
            for x in nums:
                char  = nums.pop(0)
                perms = dfs(nums)
                for y in perms:
                    y.append(char)
                    perm.append(y)
                nums.append(char)
            return perm

            
        return (dfs(nums))
        # print(res)
        