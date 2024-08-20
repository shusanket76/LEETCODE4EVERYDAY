def subsets(nums):
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
a = subsets([1,2,3])