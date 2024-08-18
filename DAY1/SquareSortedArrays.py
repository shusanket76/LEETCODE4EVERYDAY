class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums)-1
        while l<=r:
            right = nums[r]**2
            left = nums[l]**2
            if left<right:
                res.append(right)
                r-=1
            else:
                res.append(left)
                l+=1
        res = res[::-1]
        return res